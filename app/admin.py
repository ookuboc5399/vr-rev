from django.contrib import admin
from .models import Blog, Category,Product

admin.site.register(Blog)
admin.site.register(Product)
admin.site.register(Category)