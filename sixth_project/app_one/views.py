from django.shortcuts import render
from app_one.forms import UserForm

# Create your views here.

def index(request):
    return render(request, "app_one/index.html")

def user(request):
    form = UserForm()   # Getting the instance of the user form

    if request.method == "POST":    # if everything goes all okk
        form = UserForm(request.POST)   # we grab the form data

        if form.is_valid(): # check if it is valid or not
            form.save(commit=True)  # save the form to the database
            return index(request)   # return a request to the index page(basically brings us back to the index page)

        else:
            print("ERROR FORM INVALID!!")

    return render(request, "app_one/users.html", {'form': form})