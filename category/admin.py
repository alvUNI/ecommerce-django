from django.contrib import admin
from . models import Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name', )} # q se autogenere el slug
    list_display       = ('category_name', 'slug')      # para mostrar como titulos slug y category_name

admin.site.register(Category, CategoryAdmin)
