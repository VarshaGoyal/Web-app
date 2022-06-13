from django.urls import path

from . import views

urlpatterns = [
    path('' , views.home , name = 'home'),
     path('about/' , views.about , name = 'about'),
      path('about2/' , views.about2 , name = 'about2'),
]