from django.contrib import admin

# Register your models here.

from .models import Fixture

admin.site.register(Fixture)