from django.contrib import admin
from .models import PersonModel

# class PersonModelInline()

class PersonModelAdmin(admin.ModelAdmin):
    
    pass


admin.site.register(PersonModel,PersonModelAdmin)
