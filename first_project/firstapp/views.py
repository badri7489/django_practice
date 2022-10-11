from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello I am from views.py!!"}
    return render(request, 'index.html', context=my_dict)

def help(request):
    my_dict = {'fuck_me': "Hello this is from views.py file, I'm here to help you dumb fucking bitch!!"}
    return render(request, 'help.html', context=my_dict)