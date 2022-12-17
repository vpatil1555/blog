from django.urls import path
from . import views


# create a path or url for REGISTER

urlpatterns = [
    
    path("registration",views.registration,name="registration"),
    path("login",views.login,name="login")
]
