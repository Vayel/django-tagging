"""
Admin components for tagging.
"""
from django.contrib import admin

from tagging.forms import TagAdminForm
from tagging.models import Tag, TaggedItem


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm
    search_fields = ('name',)


@admin.register(TaggedItem)
class TaggedItemAdmin(admin.ModelAdmin):
    autocomplete_fields = ('tag',)
