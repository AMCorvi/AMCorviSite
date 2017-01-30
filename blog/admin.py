from django.contrib import admin

from .models import Blog, Tag
# Register your models here.

admin.site.register(Blog)

class TagsAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, { "fields": ['tag_name']}),
            ]

admin.site.register(Tag,TagsAdmin)
