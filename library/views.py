from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Test Home")


def about(request):
    return HttpResponse("Test About")
