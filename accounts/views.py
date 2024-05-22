from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    message = "welcome home from views accounts"
    data ={"msg":message}
    return render(request,"accounts/home.html",data)

