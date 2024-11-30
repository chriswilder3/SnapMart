from django.shortcuts import render,redirect

from .models import Product
# Create your views here.

def home(request):
    products = Product.objects.all()
    context ={ 'items': products } # In template it will easy
                                # to remember as items

    return render( request, 'index.html', context)

def search(request):
    searchitem = request.GET.get('searchitem')

    if searchitem != '' and searchitem is not None:
        products = Product.objects.filter( name__icontains = searchitem)
        if products.exists():
            context = {'items':products, 'searchterm':searchitem,'isSearchValid':True,'resultFound':True}
        else:
            context = {'searchterm':searchitem,'isSearchValid':True,'resultFound':False}
    else:
        # Invalid search
        context = { 'searchterm':searchitem,'isSearchValid':False}
    return render(request, 'searchresults.html', context)

