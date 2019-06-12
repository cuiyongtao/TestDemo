from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.

def index(request):  # request 必须要写，不然会报错
    return HttpResponse("hello wold")


def index2(request):
    # data = {"data": "hello worldsss"}
    datalist=[]
    for i in range(0,20):
        test="我是第"+str(i)+"个数据"
        datalist.append(test)
    return render(request, 'index2.html', {"data": datalist})
