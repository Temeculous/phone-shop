from django.contrib import admin


# Importing phone class so we can register to the admin site
from .models import Phone
# Register your models here.
admin.site.register(Phone)