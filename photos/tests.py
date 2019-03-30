from django.test import TestCase

from .models import Profile,Image,Comments

# Create your tests here.

class ProfileTestClass(TestCase):
    '''
    test for Location class
    '''

    # Set up method
    def setUp(self):
        self.prof= Profile(first_name = 'Hat', last_name ='Nic',prof_image = "drgf xghbvsk", bio = "vg fdgk dsgf")
  
    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))


class ImageTestClass(TestCase):
    '''
    test for Image class
    '''

    def setUp(self):
        self.prof= Profile(first_name = 'Hat', last_name ='Nic',prof_image = "drgf xghbvsk", bio = "vg fdgk dsgf")
        self.prof.save()  

        self.new_image= Image(image = 'bsdzsfbg.jpeg',name = 'sdgcfsdhf',caption = 'a way to live adventure',likes = 1,profile = self.prof,user = " ")
        self.new_image.save()



    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        self.new_image.save()
        new_image = Image.objects.all()
        self.assertTrue(len(new_image) > 0)

    def test_get_all_images(self):
        images = Image.get_all()
        self.assertTrue(len(images)>0)
 

    def test_search_image(self):
        images = Image.search_image('pic')
        self.assertFalse(len(images)>0)