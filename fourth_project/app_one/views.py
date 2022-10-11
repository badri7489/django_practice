from django.shortcuts import render
from app_one.models import Users

# Create your views here.

def index(request):
    my_dict = {"insert_me": "Go to app_one/users to see the list of user informations!"}
    return render(request, "app_one/index.html", my_dict)

def users(request):
    user_list = Users.objects.order_by('first_name')
    user_dict = {"insert_me": user_list}
    return render(request, "app_one/users.html", context=user_dict)