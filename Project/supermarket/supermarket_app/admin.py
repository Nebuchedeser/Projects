# admin.py
from django.contrib import admin
from django.contrib import admin

from .models import Category, SubCategory, Item


# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Item)

# Register the Category model with the admin site.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

# Register the SubCategory model with the admin site.
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass

# Register the Item model with the admin site.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
