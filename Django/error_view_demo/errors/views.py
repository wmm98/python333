from django.http import HttpResponse
from django.shortcuts import render


def view_405(request):
    return render(request, "errors/405.html")


def view_403(request):
    return render(request, "errors/403.html")