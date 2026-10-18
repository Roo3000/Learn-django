from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

#example of a function-based view
def hello_world(request):
    return HttpResponse("Hello, World!")

#example of a class-based view
class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")