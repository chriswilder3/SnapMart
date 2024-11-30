from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='index'),
    path('search', views.search, name = 'search'),
    path('product/<int:id>', views.detail, name= 'detail'),
]