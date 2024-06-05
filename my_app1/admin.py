from django.contrib import admin
from .models import Contact, PopularProduct, Newsletter

admin.site.register(Contact)
admin.site.register(PopularProduct)
admin.site.register(Newsletter)

# Register your models here.
