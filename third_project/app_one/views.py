from django.shortcuts import render
from app_one.models import Topic, AccessRecord, Webpage

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, "app_one\index.html", context=date_dict)