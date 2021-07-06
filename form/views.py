from django.shortcuts import render
from form.models import People
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        people = People(name=name, email=email)
        people.save()
    return render(request, 'index.html')