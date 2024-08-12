from django.contrib import admin
from .models import Category, Product, Order


#customize admin panel
admin.site.site_header = 'ESPOIR E-COMMERCE'
admin.site.site_title = 'ESPOIR SHOP'
admin.site.index_title = 'Espace Admin'



# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date')
    search_fields = ('title','price',)
    list_editable = ('price',)

class OrderProduct(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'amount', 'country', 'city', 'address', 'zipcode', 'date')

admin.site.register(Category, AdminCategorie)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, OrderProduct)

 