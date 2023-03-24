from django.shortcuts import render
from django.http import HttpResponse

message = "Welcome to our front end! We are Nicolas Posner and Carina Kane in CMSC 13600. Nico is a Data Science Major from Madrid, Spain. Carina does not have a bio yet."

def index(request):
    return render(request, 'app/index.html', {"message": message})
