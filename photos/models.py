from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to ="images/")
    bio = models.CharField(max_length =700)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.user_name

    def save_profile(self):
        self.save() 

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
    Profile = models.ForeignKey(Profile)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
     
    def update_caption(self):
        self.update_caption()

    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(pub_date__date = today)
        return photos

    @classmethod
    def days_photos(cls,date):
        photos = cls.objects.filter(pub_date__date = date)
        return photos

    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos

class PhotosRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.TextField()

class Comment(models.Model):
    profile = models.ForeignKey(Profile, null=True)
    comment = models.CharField(max_length =100)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
            return self.user_name

    def save_commet(self):
        self.save()

    def delete_commet(self):
        self.delete()
        
    def __str__(self):
            return self.name   
     
    


