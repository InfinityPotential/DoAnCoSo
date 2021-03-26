from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    respone = HttpResponse()
    respone.writelines('<h1>Hello World</h1>')
    respone.write('This is app home')
    return respone