from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {"insert_me": "I am the index Page!!"}
    return render(request, "app_one\index.html", my_dict)

def help(request):
    my_dict = {"fuck_me": "I am the help Page!!"}
    return render(request, "app_one\help.html", my_dict)

def django(request):
    my_dict = {"fuck_you": "I am the django Page!!"}
    return render(request, "app_one\django.html", my_dict)