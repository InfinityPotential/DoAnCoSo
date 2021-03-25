from django.shortcuts import render
from django.http import HttpRespone
# Create your views here.
def index(request):
    respone = HttpRespone()
    respone.writelines('<h1>Hello world</h1>')
    respone.write('This is app Home')
    return respone