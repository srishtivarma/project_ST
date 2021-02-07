from django.contrib import admin
from django.urls import path
from app.views import home, create


urlpatterns = [
    path('', home, name='home'),
    path('create', create, name='create')
]
