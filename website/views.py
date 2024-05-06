from django.http import HttpResponse
from django.shortcuts import render


def dashboard(request):
    context ={"numbers":[1,2,3,4,5],
              "names" :["apple","Boy" ,"Cat"],
              }
    return render(request,"dashboard.html",context)

def home(request):
    message = "welcome home from views again"
    data ={"msg":message}
    return render(request,"home.html",data)