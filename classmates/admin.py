from django.contrib import admin

# Register your models here.
from .models import Mamber

class MamberAdmin(admin.ModelAdmin):
    list_display=("id","name")
    prepopulated_fields = {"slug":("name",)}


admin.site.register(Mamber, MamberAdmin)
