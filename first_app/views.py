from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,WebPage,AccessRecord
# Create your views here.
def index(request):
    WebPage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':WebPage_list,'my_name':"Rujal Shrestha"}
    #my_dict = {'my_name': "Rujal Shrestha"}
    return render(request,"first_app/index.html",context=date_dict)
