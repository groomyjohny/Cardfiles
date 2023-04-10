from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Картотека на производстве")

# Create your views here.
