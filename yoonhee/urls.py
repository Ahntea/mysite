from django.urls import path

from . import views

app_name = 'yoonhee'

urlpatterns = [
    path('', views.index, name='index'),
]