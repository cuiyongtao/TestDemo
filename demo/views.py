from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(reques):#request 必须要写，不然会报错
    return HttpResponse("hello wold")
