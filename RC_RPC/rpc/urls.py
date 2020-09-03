
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('success',views.success,name="success"),
]
