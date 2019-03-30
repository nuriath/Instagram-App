from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to ="images/")
    bio = models.CharField(max_length =700)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.user_name

    def save_profile(self):
        self.save() 
    
    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profile = cls.objects.all()
        return profile

    @classmethod
    def search_by_username(cls,search_term):
        profile = cls.objects.filter(first_name__icontains=search_term)
        return profile

    class Meta:
        ordering = ['user_name']   

class likes(models.Model):
    name = models.CharField(max_length =30)

     
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to ='images/', blank=True)
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    Profile = models.ForeignKey(Profile,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.image_name


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
     
    @classmethod
    def get_image(cls):
        image = cls.objects.all()
        return image    
   
class Comment(models.Model):
    profile = models.ForeignKey(Profile, null=True)
    comment = models.CharField(max_length =100)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    def save_commet(self):
        self.save()

    def delete_commet(self):
        self.delete()
        
class Like(models.Model):
    likes= models.IntegerField(default=0)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.like 
    


