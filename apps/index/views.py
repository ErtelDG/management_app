from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("HALLO HERE IS THE INDEX START FOR THE MANAGEMENT APP.")