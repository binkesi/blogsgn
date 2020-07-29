from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Article)
admin.site.register(models.Author)

@admin.register(models.Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'article', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)