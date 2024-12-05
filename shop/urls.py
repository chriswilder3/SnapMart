from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='index'),
    path('search', views.search, name = 'search'),
    path('product/<int:id>', views.detail, name= 'detail'),
    path('cartview', views.cart_view, name = 'cartview'),
    path('cartview/delete', views.cart_delete, name='cartDelete'),
    path('master', views.master, name='master'),
    path('categories/<str:category>', views.categories, name='categories'),
    path('checkout', views.checkout, name='checkout'),
    path('order', views.order, name = 'order'),
]