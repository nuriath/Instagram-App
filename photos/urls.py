from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.photos_today,name='photos_of_day'),
    url(r'^new/image$', views.new_image, name='new_image'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^view/profile/(\d+)', views.view_profile, name='view_profile'),
    url(r'^comment/(\d+)', views.comment, name='comment'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)