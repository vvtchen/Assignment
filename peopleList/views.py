import json
from .models import People
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import PeopleSerializer, QuerySerializer
from drf_spectacular.utils import extend_schema

# Create your views here.
@extend_schema(request=PeopleSerializer, responses=None)
@api_view(["POST"])
def createNew(request):
    if request.method == 'POST':
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            existed = People.objects.filter(**serializer.validated_data)
            if not existed:
                serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@extend_schema(responses=QuerySerializer)
@api_view(["GET"])
def all(request):
    if request.method == 'GET':
        people = People.objects.all()
        serializer = QuerySerializer(people, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@extend_schema(responses=None)
@api_view(["DELETE"])
def delete(request, id):
    if request.method == 'DELETE':
        target = People.objects.filter(pk = id);
        target.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@extend_schema(responses=None, request=dict)
@api_view(["PUT"])     
def update(request, id):
    if request.method =="PUT":
        target = People.objects.filter(pk=id);
        if not target.exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            data = json.loads(request.body.decode('utf-8'))
            if data:
                target.update(**data)
                return Response(status=status.HTTP_200_OK)      
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@extend_schema(request=PeopleSerializer(many=True), responses=None)
@api_view(["POST"])
def templateCreate(request):
    if request.method == "POST":
        serializer = PeopleSerializer(data=request.data, many=True)
        print (serializer)
        duplicateList = []
        newList = []   
        if serializer.is_valid():
            for people in serializer.data:
                existed = People.objects.filter(**people)
                if not existed.exists():
                    newList.append(People(**people))
                else:
                    duplicateList.append(people)
            if newList:
                People.objects.bulk_create(newList)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)