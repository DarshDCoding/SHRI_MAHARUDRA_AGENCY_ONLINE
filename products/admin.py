from django.contrib import admin
from .models import Product, ProductImages, HSN, Company

# Register your models here.
@admin.register(Product)
class ProductManager(admin.ModelAdmin):
    list_display = ('pk', 'name', 'packing','get_company','mrp', 'quantity', 'is_available')
    list_select_related = ('company',)

@admin.register(ProductImages)
class ProductImageManager(admin.ModelAdmin):
    list_display = ('product_name', 'is_primary', 'created_at', 'updated_at')
    list_select_related = ('product',)

@admin.register(HSN)
class HSNManager(admin.ModelAdmin):
    list_display = ('hsn_number', 'sgst', 'cgst', 'gst')

@admin.register(Company)
class CompanyManager(admin.ModelAdmin):
    list_display = ('name', 'created_at')

