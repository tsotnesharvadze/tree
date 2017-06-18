from django.contrib import admin
from .models import PersonModel

# class PersonModelInline()

class PersonModelAdmin(admin.ModelAdmin):
    search_fields=['name','parent__name']


admin.site.register(PersonModel,PersonModelAdmin)
