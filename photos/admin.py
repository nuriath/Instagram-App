from django.contrib import admin
from .models import Profile,Image,Comments
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('likes',)

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comments)
