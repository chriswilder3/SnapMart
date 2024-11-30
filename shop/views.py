from django.shortcuts import render,redirect

from .models import Product
# Create your views here.

def home(request):
    products = Product.objects.all()
    context ={ 'items': products } # In template it will easy
                                # to remember as items
    return render( request, 'index.html', context)

