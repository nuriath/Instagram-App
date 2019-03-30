from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import ProfileForm,ImageForm,CommentsForm,LikeForm
from .models import Image,Profile,Comments,Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()

    profile = Profile.objects.all()
    return render(request,'index.html',{"images":images,"profile":profile})

@login_required(login_url='/accounts/login/')
def com(request,image_id):
    image = Image.objects.get(id = image_id)
    comments = Comments.objects.filter(image = image.id).all() 
    likes = Like.objects.filter(image = image.id).all() 

    return render(request,'inde.html',{"image":image,"comments":comments,"likes":likes})

@login_required(login_url='/accounts/login/')
def images(request,image_id):
    image = Image.objects.get(id = image_id)
    return render(request,"info.html", {"image":image})

@login_required(login_url='/accounts/login/')
def myProfile(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.get(user = user)
    images = Image.objects.filter(user = user).all()
   
    return render(request,'view_profile.html',{"profiles":profiles,"user":user,"images":images})

def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect(home)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

def image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()

            return redirect(home)

    else:
        form = ImageForm()
    return render(request, 'new_image.html', {"form": form})

def comments(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.user = current_user
            comments.save()

            return redirect(home)

    else:
        form = CommentsForm()
    return render(request, 'comment.html', {"form": form})


def like(request):
    current_user = request.user
    if request.method == 'POST':
        form = LikeForm(request.POST, request.FILES)
        if form.is_valid():
            likes = form.save(commit=False)
            likes.user = current_user
            likes.save()

            return redirect(home)

    else:
        form = LikeForm()
    return render(request, 'like.html', {"form": form})
