from rest_framework import serializers
from usadata.models import State, Person

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        
    def validate(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        if Person.objects.filter(first_name=first_name, last_name=last_name).exists():
            if self.instance is not None:
                if self.instance.first_name == first_name and self.instance.last_name == last_name:
                    return data
            raise serializers.ValidationError("A person with this first and last name already exists.")

        return data
