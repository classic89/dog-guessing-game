from django.shortcuts import render, HttpResponse

# Create your views here.
def my_view(request):
    return HttpResponse( "Hello, world. You're at the polls index." )