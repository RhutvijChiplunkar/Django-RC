from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Blog-home'),
    path('about/',views.about,name='Blog-about'),
    path('nos/',views.nos,name="case-1")
]
