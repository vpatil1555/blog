from django.urls import path

from . import views

# create a path or url

urlpatterns = [
    
    path('',views.index,name='home')
]
