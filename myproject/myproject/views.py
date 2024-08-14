from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("fuck the world")


def about(request):
    return render(request,"index.html")