from .views import *
from django.urls import path

urlpatterns = [
path('register/', RegisterUser.as_view()),    
path('allusers/', Profiles.as_view()),
path('user/<str:pk>',Profile.as_view()),
]
