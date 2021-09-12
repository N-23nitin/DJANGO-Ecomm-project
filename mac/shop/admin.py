from django.contrib import admin
from .models import Product, Contact, Orders, OrderUpdate
# Register your models here.
# @admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
   list_display = ['product_name', 'category', 'price', 'pub_date']

class ContactAdmin(admin.ModelAdmin):
   list_display = ['name', 'email', 'phone']

class OrderAdmin(admin.ModelAdmin):
   list_display = ['name','amount', 'email','address', 'phone', 'city', 'state', 'zip_code']

class UpdateAdmin(admin.ModelAdmin):
   list_display = ['order_id', 'timestamp']

admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Orders, OrderAdmin)
admin.site.register(OrderUpdate, UpdateAdmin)
