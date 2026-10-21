from django.urls import path
from . import views

urlpatterns = [
    #acessing the function-based view
    path('function', views.hello_world),
    #accessing the class-based view
    path('class', views.HelloWorldView.as_view()),
    #accessing my reservation form
	path('reservation', views.home),
]