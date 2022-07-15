from django.contrib import admin
from .models import Program, Item



class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)



class ProgramAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'type']

admin.site.register(Program, ProgramAdmin)