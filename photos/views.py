from .forms import InstagramForm
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comments
import datetime as dt
from .forms import NewImageForm, ProfileForm,CommentsForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def photos_of_day(request):
    date = dt.date.today()
    photos = Image.objects.all()
    return render(request, 'all-pictures/today-pictures.html', {'pictures':pictures})

