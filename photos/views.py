
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment
import datetime as dt
from .forms import NewImageForm, ProfileForm,CommentForm
from .email import send_welcome_email

# Create your views here.
@login_required(login_url='/accounts/login/')
def photos_of_day(request):
    date = dt.date.today()
    photos = Image.objects.all()
    return render(request, 'all-photos/today_photos.html', {'photos':photos})

@login_required(login_url='/accounts/login/')
def photos_today(request):
    if request.method == 'POST':
        form = NewImageForm(request.POST)
        if form.is_valid():
            print('valid')
        form = NewImageForm(request.POST)
    else:
        form = CommentForm()

        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = PhotosRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('photos_today')
        else:
            form = NewImageForm()
    return render(request, 'all-photos/today_photos.html', {"NewImageForm":form})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('photos_today')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect(profile)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def view_profile(request, id):

    profile=Profile.objects.get(user_name_id=id)
    photos = Image.objects.filter(id=id)
    return render(request, 'view_profile.html',{"profile":profile , "photos":photos},)

def comment(request, id):
    current_user = request.user
    post = Image.objects.get(id=id)
    comments1 = Comment.objects.filter(image=post)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.cleaned_data['comment']
            new_comment = Comment(comment = comment,user =current_user,image=post)
            new_comment.save()

    else:
        form = CommentForm()
    return render(request, 'comments.html', {"form":form,'post':post,'user':current_user,'comment':comment1})
