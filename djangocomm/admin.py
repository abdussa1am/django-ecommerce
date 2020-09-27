from django.contrib import admin

# Register your models here.

from .models import Category, Product , Cart , Order

class ProductAdmin(admin.ModelAdmin):
      list_display = ('name', 'category' , 'price' , 'mainimage')
      ordering = ('name',)
      search_fields = ('name',)
class OrderAdmin(admin.ModelAdmin):
      list_display = ( 'user' , 'created' , 'get_parents')
      ordering = ('created',)
      search_fields = ('name',)
admin.site.register(Category)
admin.site.register(Product , ProductAdmin)
admin.site.register(Cart)
admin.site.register(Order , OrderAdmin)