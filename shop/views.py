from django.shortcuts import render,redirect

from .models import Product

from django.core.paginator import Paginator

import json

# Create your views here.

def home(request):
    products = Product.objects.all()

    paginator = Paginator(products,8)
    # Page no 
    page_num = request.GET.get('page')

    page_obj = paginator.get_page(page_num)
    
    context ={ 'items': page_obj } # In template it will easy
                                # to remember as items

    return render( request, 'index.html', context)

#-----------------Search Result page
def search(request):
    searchitem = request.GET.get('searchitem')

    if searchitem != '' and searchitem is not None:
        products = Product.objects.filter( name__icontains = searchitem)
    
        if products.exists():
            paginator = Paginator(products,4)
            page_num = request.GET.get('page') 
            page_obj = paginator.get_page(page_num)

            context = {'items':page_obj, 'searchterm':searchitem,'isSearchValid':True,'resultFound':True}
        else:
            context = {'searchterm':searchitem,'isSearchValid':True,'resultFound':False}
    else:
        # Invalid search
        context = { 'searchterm':searchitem,'isSearchValid':False}
    
    # V.IMP : Make sure the page nav buttons also return searchitem again back
    # along with page. 
    # ex : href="?page={{items.previous_page_number}}&searchitem={{searchterm}}"
    # Why?
    # Becase these buttons are links hence they make GET requests and if they
    # dont sent searchitem along with them, it will trigger invalid searchitem
    # ifelse case above.

    return render(request, 'searchresults.html', context)

# -----------Product detail view

def detail( request, id):
    # The id will be passed as path param, when we click on an itemcard
    # which is the same id received here.

    product = Product.objects.get(id= id)
    # Get a single object only

    # Create a detail.html now
    return render( request, 'detail.html', {'item':product})



def cart_view(request):
    # This is the view that passes information of all elements in the cart
    # to show in the cartview template.

    # Further We optimized this, such that we receive the
    # cart elemts here directly and fetch them Here.

    cartData = request.POST.get('cartData')

    if cartData:
        # if cart is not empty
        cartData = json.loads(cartData)
        # print(cartData)
        print(cartData)
        # Now for all the keys in the above object, we get corrsponding items

        items = Product.objects.none()
        # This creates an empty queryset to which we can append specific 
        # cart products.
        # Learn more on queryset objects here : https://chatgpt.com/share/674ccec2-24ec-8002-967d-3eebcd196b2c
        # and through ChatGPT PDF : Queryset IMP operations.pdf

        for key,val in cartData.items():
            # print(key, val)
            prod = Product.objects.filter(id = key)
            items = items | prod  # This combines items queryset with prod each time
        # print(items)
        context = {
            'items' : items,
            'cartCount': cartData,
            'cartEmpty':False,
        }
        print( type(cartData))
    else:
        context = {
            'cartEmpty':True,
        }
    return render(request, 'cartview.html',context)

    
