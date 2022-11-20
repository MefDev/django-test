from django.shortcuts import render
from django.http import HttpResponse
# request handlers..(the exact name)
# Create your views here.

def say_hello(request):
    return render(request, 'hello.html', {'name': 'G'})
