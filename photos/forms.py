from .models import Profile,Image,Comments,Like
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user']

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = ['user']
