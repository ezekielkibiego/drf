from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    roll_number = serializers.IntegerField()
    mobile = serializers.CharField(max_length=13)
    
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'address', 'roll_number', 'mobile']
        read_only_field = ['id']
    