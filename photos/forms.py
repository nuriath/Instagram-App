from django import forms
from .models import Image, Profile, Comment


class CommentForm(forms.Form):
    comment = forms.CharField(label='Comment',max_length=100)

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'pub_date','likes']
     

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'pub_date','likes']
