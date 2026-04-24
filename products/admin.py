from django.contrib import admin
from .models import Product, PreOrder, DeviceModel, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Show one extra empty form


@admin.register(DeviceModel)
class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'is_active')
    list_filter = ('brand',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price_ks', 'is_active')
    list_filter = ('category', 'brand', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('compatible_models',)  # nice UI for M2M
    inlines = [ProductImageInline]


@admin.register(PreOrder)
class PreOrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'product', 'device_model', 'quantity', 'paid', 'created_at')
    list_filter = ('paid', 'product__category', 'product__brand')
    search_fields = ('full_name', 'email', 'phone')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'order')
    list_filter = ('product__category', 'product__brand')