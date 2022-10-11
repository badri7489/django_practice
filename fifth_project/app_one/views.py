from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request, "app_one/index.html")

def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            # Do something with the form
            print("Validation Successfull!!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("text: " + form.cleaned_data['text'])

    form_dict = {"form": form}
    return render(request, "app_one/form_page.html", form_dict)