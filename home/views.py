from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myindex(request):
    return HttpResponse("This is a home page")