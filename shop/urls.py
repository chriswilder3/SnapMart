from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='index'),
    path('search', views.search, name = 'search'),
    path('product/<int:id>', views.detail, name= 'detail'),
    path('cartview', views.cart_view, name = 'cartview'),
    path('master', views.master, name='master'),
    path('categories/<str:category>', views.categories, name='categories'),
    path('checkout/<int:id>', views.checkout, name='checkout'),
]