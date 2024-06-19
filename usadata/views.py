from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from usadata.models import State, Person
from usadata.serializers import StateSerializer, PersonSerializer
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter

class StateList(APIView):
    @extend_schema(
        responses={200: StateSerializer(many=True)},
        description="Retrieve a list of states"
    )
    def get(self, request, *args, **kwargs):
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response({'status': 'success', 'states': serializer.data}, status=status.HTTP_200_OK)

    @extend_schema(
        request=StateSerializer,
        responses={201: StateSerializer},
        description="Create a new state"
    )
    def post(self, request, *args, **kwargs):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class StateDetail(APIView):
    def get_object(self, id):
        try:
            return State.objects.get(id=id)
        except State.DoesNotExist:
            return None

    @extend_schema(
        responses={200: StateSerializer},
        description="Retrieve a state by ID"
    )
    def get(self, request, id, *args, **kwargs):
        state = self.get_object(id)
        if state is None:
            return Response({'status': 'error', 'data': 'State not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StateSerializer(state)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    @extend_schema(
        request=StateSerializer,
        responses={200: StateSerializer},
        description="Update a state by ID"
    )
    def put(self, request, id):
        state = self.get_object(id)
        serializer = StateSerializer(state, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={200: None},
        description="Delete a state by ID"
    )
    def delete(self, request, id, *args, **kwargs):
        state = self.get_object(id)
        if state is None:
            return Response({'status': 'error', 'data': 'State not found'}, status=status.HTTP_404_NOT_FOUND)
        state.delete()
        return Response({'status': 'success', 'data': 'State deleted successfully'}, status=status.HTTP_200_OK)

class PersonList(APIView, PageNumberPagination):
    @extend_schema(
        parameters=[OpenApiParameter(name='page', description='Page number', required=False, type=int)],
        responses={200: PersonSerializer(many=True)},
        description="Retrieve a list of people"
    )
    def get(self, request):
        people = Person.objects.all()
        results = self.paginate_queryset(people, request, view=self)
        serializer = PersonSerializer(results, many=True)
        return self.get_paginated_response({
            'message': 'People retrieved successfully',
            'people': serializer.data
        })

    @extend_schema(
        request=PersonSerializer,
        responses={201: PersonSerializer},
        description="Create a new person"
    )
    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        if Person.objects.filter(first_name=first_name, last_name=last_name).exists():
            return Response({
                'message': 'Error creating person',
                'errors': 'A person with this name already exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Person created successfully',
                'people': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Error creating person',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class PersonDetail(APIView):
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    @extend_schema(
        responses={200: PersonSerializer},
        description="Retrieve a person by ID"
    )
    def get(self, request, pk):
        person = self.get_object(pk)
        serializer = PersonSerializer(person)
        return Response({
            'message': 'Person retrieved successfully',
            'people': serializer.data
        }, status=status.HTTP_200_OK)

    @extend_schema(
        request=PersonSerializer,
        responses={200: PersonSerializer},
        description="Update a person by ID"
    )
    def put(self, request, pk):
        person = self.get_object(pk)
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        if Person.objects.filter(first_name=first_name, last_name=last_name).exclude(pk=pk).exists():
            return Response({
                'message': 'Error updating person',
                'errors': 'A person with this name already exists'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Person updated successfully',
                'people': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Error updating person',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={204: None},
        description="Delete a person by ID"
    )
    def delete(self, request, pk):
        person = self.get_object(pk)
        person.delete()
        return Response({
            'message': 'Person deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)
