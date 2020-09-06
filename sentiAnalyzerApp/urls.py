from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='sentianalyzer'),
    url(r'^predictsentiment', views.predict, name='predictsentiment'),
]