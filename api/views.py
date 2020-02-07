from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import User
import json

@csrf_exempt
def view_get_post_user(request):
    print("What's the request => ",request.method)
    if request.method == "GET":
        user = User.objects.all()
        print("QuerySet objects => ",user)
        list_of_users = list(user.values("user_name","user_email","user_address","user_gender","user_age"))
        print("List of user => ",list_of_users)
        dictionary_name = {
        "users":list_of_users
    }
        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))
        print(python_dictionary_object['user_name'])
        print(python_dictionary_object['user_email'])
        print(python_dictionary_object['user_address'])
        print(python_dictionary_object['user_gender'])
        print(python_dictionary_object['user_age'])
        User.objects.create(user_name=python_dictionary_object['user_name'],
        user_email=python_dictionary_object['user_email'],
        user_address=python_dictionary_object['user_address'],
        user_gender=python_dictionary_object['user_gender'],
        user_age=python_dictionary_object['user_age']),

        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        user = user.objects.get(id = ID)
        print(type(user.user_name))
        return JsonResponse({
            "user_name":user.user_name,
            "user_email":user.user_email,
            "user_address":user.user_address,
            "user_gender":user.user_gender,
            "user_age":user.user_age,
        })
    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        }) 