from django.test import TestCase
from .models import Image,Comments,Likes

# Create your tests here.

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.img= Image( image ='image/download_EV7vpwu.jpeg ',image_name = 'land', image_caption ='this is a picture of land',)
