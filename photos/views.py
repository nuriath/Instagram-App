from .forms import InstagramForm
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comments
import datetime as dt


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'welcome.html')

def image_today(request):
    date = dt.date.today()
    
    return render(request, 'all-news/today-news.html', {"date": date,"news":news})

