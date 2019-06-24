from django.shortcuts import render
from django.http import HttpResponse
from demo.models import UserInfo
import json

# Create your views here.

def index(request):  # request 必须要写，不然会报错
    return HttpResponse("hello wold")


def index2(request):
    # data = {"data": "hello worldsss"}
    datalist = []
    for i in range(0, 20):
        test = "我是第" + str(i) + "个数据"
        datalist.append(test)

    return render(request, 'index2.html', {"data": datalist})


userList = []


def login(request):
    if request.method == "POST":
        # 接受用户名
        username = request.POST.get("username")
        # 接收密码
        password = request.POST.get("password")
        # 添加到列表
        # userList.append({"username":username,password:password})
        # 添加到数据
        UserInfo.objects.create(usrename=username, password=password)
        #获取表中所有数据
        userList=UserInfo.objects.all()
        # 打印接收的数据
        print(userList)
        return render(request, "login.html", {"data": userList})
    elif request.method == "GET":
        return render(request, "login.html")
