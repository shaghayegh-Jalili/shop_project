from django.contrib import admin
from . import models

# admin.site.register(models.Cart)
# admin.site.register(models.Category)
# admin.site.register(models.Order)
admin.site.register(models.OrderProduct)
# admin.site.register(models.Product)


class CategoryAdmin(admin.ModelAdmin):  # the class shows some features about the category
    list_display = ['id', 'title']
    search_fields = ['title']

    def delete_queryset(self, request, queryset):
        for category in queryset:
            category.delete()


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'quantity', 'status']
    search_fields = ['title']
    list_filter = ['status']

    def delete_queryset(self, request, queryset):
        for product in queryset:
            product.delete()


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'quantity']

    def delete_queryset(self, request, queryset):
        for cart in queryset:
            cart.delete()


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_price', 'status']
    list_filter = ['status']


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Cart, CartAdmin)
