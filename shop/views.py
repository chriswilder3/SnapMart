from django.shortcuts import render,redirect

from django.http import HttpResponse

from .models import Product, Order

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
        # print( type(cartData))
    else:
        context = {
            'cartEmpty':True,
        }
    return render(request, 'cartview.html',context)

def cart_delete( request ):
    data = request.POST.get('items')
    deleteId = request.POST.get('id')
    # print(data)
    # if data:
    #     data = json.loads(data)
    #     print(type(data))
    print(deleteId)
    #a = data.filter(id = deleteId)
    #print(a)
    return HttpResponse('Hi')

    
def master( request):
    # This view is used to send categories to master on any page
    # It send all categories as httpreonse to a JS script on master page

    categories = Product.objects.all().values_list('category' ,flat = True)
    categories = list(set(categories)) # get unique values
    # get unique values of list
    # print(categories)
    
    context = {
        'categories' :categories,
    }
    # return HttpResponse(json.dumps(context))
    return HttpResponse(json.dumps(context))

def categories( request, category):

    products = Product.objects.filter(category = category)

    paginator = Paginator(products,4)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    context ={ 'items': page_obj,
                'category':category,
            } 
    return render( request, 'categories.html', context)

def checkout(request):
    totalPrice = request.POST.get('finalPrice')
    context ={
        'price': totalPrice,
    }
    return render(request, 'checkout.html', context)

def order(request):
    cartData = request.POST.get('cartData')
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    pincode = request.POST.get('pincode')

    order = Order(items = cartData, first_name= first_name, last_name = last_name, phone= phone, email= email, address =address, city = city, state =state, pincode = pincode)
    order.save()

    context ={

    }
    return render(request, 'order.html', context)

    