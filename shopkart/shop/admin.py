from django.contrib import admin
from .models import *

# Register your models here.
"""
class CatagoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description')
admin.site.register(Catagory,CatagoryAdmin)
 user page la image name description display pannurakkaga idhu
"""
admin.site.register(Catagory)
admin.site.register(product)