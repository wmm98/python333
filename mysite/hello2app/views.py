from django.shortcuts import render


def hello(request):
    return render(request, 'PYC01-HTMLJSDemo.html')
