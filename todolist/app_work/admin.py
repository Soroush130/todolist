from django.contrib import admin
from .models import Work, TypeWork, Tag, Score


class WorkAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'start_work', 'end_work', 'user', 'is_finished']
    # pass


admin.site.register(Work, WorkAdmin)


class TypeWorkAdmin(admin.ModelAdmin):
    pass


admin.site.register(TypeWork, TypeWorkAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent', 'user']


admin.site.register(Tag, TagAdmin)


admin.site.register(Score)
