from .forms import InstagramForm
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment
import datetime as dt
from .forms import NewImageForm, ProfileForm,CommentForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def photos_of_day(request):
    date = dt.date.today()
    photos = Image.objects.all()
    return render(request, 'all-photos/today-photos.html', {'photos':photos})

@login_required(login_url='/accounts/login/')
def photos_today(request):
    if request.method == 'POST':
        form = PhotosLetterForm(request.POST)
        if form.is_valid():
            print('valid')
        form = PhotosLetterForm(request.POST)
    else:
        form = NewsLetterForm()

        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = PhotosRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('photos_today')
        else:
            form = PhotosForm()
    return render(request, 'all-photos/today-photos.html', {"photos":photos,"PhotosForm":form})
