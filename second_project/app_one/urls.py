from django.urls import path
from app_one import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("help", views.help, name = "help"),
    path("django", views.django, name = "django")
]