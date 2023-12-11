from django.shortcuts import render, HttpResponse

# Create your views here.

# atomic transaction

# view
# class based view
# function based view

from .models import Student

# view -- function based view
# def welcome(request): # reserved keyword    # business logic
    # print(request.method)
    # print(request.user)
    # print(request.__dict__)
    # print(request.GET(["age"])) # http://127.0.0.1:8000/welcome/?name=abc&surname=pqr&age=25
    # studs = Student.objects.get(id =2)
    # studs = Student.objects.values("name")
    # final_studs = list(map(lambda x:x["name"], studs))
    # return HttpResponse(f"Welcome to Django Application...!!!, {final_studs}") 

def welcome(request):
    return render(request, "home.html")

# query params - Query Parameters
    