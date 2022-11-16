from django.urls import path
from .views import *

urlpatterns = [
    path('all',AllProducts.as_view()),
    path('create',CreateProductAPI.as_view()),
    path('crud/<str:pk>', ProductAPI.as_view()),
]
