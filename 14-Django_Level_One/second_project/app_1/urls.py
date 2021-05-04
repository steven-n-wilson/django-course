from django.conf.urls import url
from django.urls.conf import path
from app_1 import views

urlpatterns = [
  path('', views.help, name='help'),
]
