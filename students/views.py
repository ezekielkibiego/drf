from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from students import serializers
from students.models import Student
from students.serializers import StudentSerializer

class StudentListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({'status': 'success', 'students': serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class StudentDetailView(APIView):
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return None
        
    def get(self, request, id, *args, **kwargs):
        student = self.get_object(id)
        if student is None:
            return Response({'status': 'error', 'data': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student)
        
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
    
    def delete(self, request, id, *args, **kwargs):
        student = self.get_object(id)

        if student is None:
            return Response({'status': 'error', 'data': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response({'status': 'success', 'data': 'Student deleted successfully'}, status=status.HTTP_200_OK)
