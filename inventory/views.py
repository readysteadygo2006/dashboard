from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "inventory/home.html")


def away(request):
    return HttpResponse("Away, World!")