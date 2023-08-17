from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json
from .models import People
# Create your views here.

def createNew(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        name = data.get('name')
        position= data.get('position')
        department= data.get('department')
        education= data.get('education')
        degree= data.get('degree')
        email= data.get('email')
        address= data.get('address')
        postalCode= data.get('postalCode')
        
        people = People(name=name, position=position, department=department, education=education, degree=degree, email=email, address=address, postalCode=postalCode)
        people.save()

        return JsonResponse({
            "success": True,
        })
    else:
        return HttpResponseBadRequest("Only Post requests are allowed")
    
def all(request):
    if request.method == 'GET':
        people = People.objects.all()
        data = serialize('json', people)
        parsed_data = json.loads(data)
        return JsonResponse(parsed_data, safe=False)
    else:
        return HttpResponseBadRequest("Only Get requests are allowed")
    

def delete(request, id):
    if request.method == 'DELETE':
        target = People.objects.filter(pk = id);

        if not target.exists():
            return JsonResponse({
                "success": False,
            })
        else:
            target.delete()
            return JsonResponse({
                "success": True,
            })
    else:
        return HttpResponseBadRequest("Only Delete requests are allowed")
    
        
def update(request, id):
    if request.method =="PUT":
        target = People.objects.filter(pk=id);
        if not target.exists():
            return JsonResponse({
                "success":False,
                "reason":"The User does not exist"
            })
        else:
            data = json.loads(request.body.decode('utf-8'))
            target.update(**data) #** syntax to unpack the dictionary as keyword arguments
            return JsonResponse({
                "success":True,
            },status=200)
            
    else:
        return HttpResponseBadRequest("Only Post requests are allowed")
    

def templateCreate(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'));
        duplicateList = []
        newList = []
        
        for people in data:
            existed = People.objects.filter(**people)
            if not existed.exists():
                newList.append(People(**people))
            else:
                duplicateList.append(people)

        if newList and not duplicateList:
            People.objects.bulk_create(newList)
            return JsonResponse({
                "success":True,
            }, status=200)
        elif not newList:
            return JsonResponse({
                "success": False,
                "issue":duplicateList,
                "message": "全部資料重複存在資料庫中"
            }, status=200)
        else:
            People.objects.bulk_create(newList)
            return JsonResponse({
                "success": True,
                "issue":duplicateList,
                "message": "部分存在資料庫中"
            },status=200)
    else:
        return HttpResponseBadRequest("Only Post requests are allowed")