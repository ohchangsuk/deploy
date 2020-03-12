from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('phar', views.phar, name='phar'),
    path('More', views.More, name='More'),
]
