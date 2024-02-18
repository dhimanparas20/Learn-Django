from django.shortcuts import render 
from django.http import JsonResponse

def index(request):
    data = {"location": "Inside API"}
    return JsonResponse(data)    