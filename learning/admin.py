from django.contrib import admin
from learning.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "created"]

admin.site.register(Product,ProductAdmin)
admin.site.site_header = "admin baslk"
admin.site.site_title = "admin baslk"
admin.site.index_title = "admin baslk"