from django.shortcuts import render,HttpResponse
import datetime
from blogapp import models
# Create your views here.
user_list=[]
def cur_time(request):
    # return HttpResponse("<h1>Hello H1</h1>")
    curentTime=datetime.datetime.now()
    return render(request,'cur_time.html',{"time":curentTime})


def userInfo(request):
    if request.method=="POST":
        name=request.POST.get("username","SB")
        sex=request.POST.get("sex","None")
        mail=request.POST.get("mail","Secert")
        print(name,sex,mail)

        models.Userinfo.objects.create(
            username=name,
            sex=sex,
            email=mail,
        )
        user_list=models.Userinfo.objects.all()
        return render(request,"index.html",{"user_list":user_list})
    return render(request,"index.html")