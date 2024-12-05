from django.contrib import admin
from .models import Product
# Register your models here.
from .models import Order





# Changing appearance of admin panel
admin.site.site_header = 'Snap Mart Admin' 
        # site_header is a property/ attr. used to set the big heading in admin
admin.site.site_title = 'snapmart admin' 
        # sets browser tab title (useless)

# To make specific fields appear on admin, make a class deriving ModelAdmin
# and assign list of such fields to a property called list_display

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','discount_price', 'category']

    # We can also enable searching inside admin panel for this pass the
    # the fields which are searchable to search_fields attr.
    search_fields = ['name', 'category']

    # To add custom actions other than deletion, when we select multiple 
    # elements in admin, we can do that by defining method here
    # and puting them in a list and assign to actions property.

    def change_category_to_specified(self, request, queryset):
        # Here we need queryset to perform action on the model
        # To set category to another value, just use queryset 
        # operation 'update'
        queryset.update(category = 'default')
    actions = ['change_category_to_specified',]



# When we use such classes, we need to pass them along with related models
# to the site.register
admin.site.register(Product, ProductAdmin)


# Lets do the same for Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','price', "created_at"]

admin.site.register(Order, OrderAdmin)



