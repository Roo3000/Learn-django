from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm
# Create your views here.

#example of a function-based view
def hello_world(request):
    return HttpResponse("Hello, World!")

#example of a class-based view
class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")

def home(request):
    form = ReservationForm()
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reservation successful!")
    return render(request, 'index.html', {'form': form})