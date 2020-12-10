from django.contrib import admin

# Register your models here.
from .models import Entity
class EntityAdmin(admin.ModelAdmin):
    list_display=('id','token','tsync_id')
admin.site.register(Entity,EntityAdmin)