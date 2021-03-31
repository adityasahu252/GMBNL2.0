from django.contrib import admin
from .models import Coustmer
# Register your models here.

@admin.register(Coustmer)

class coustmeradmin(admin.ModelAdmin):
    list_display=['id','name','phone_number','username','password']