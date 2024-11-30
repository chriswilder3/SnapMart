from django.shortcuts import render,redirect

from .models import Product

from django.core.paginator import Paginator
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

