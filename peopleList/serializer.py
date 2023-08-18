from rest_framework import serializers
from .models import People

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields=("pk", "name", "position", "department", "education", "degree", "email", "address", "postalCode" )

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields=("name", "position", "department", "education", "degree", "email", "address", "postalCode" )