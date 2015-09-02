# -*- coding: utf-8 -*-

from django.contrib import admin

from adminsortable.admin import SortableAdmin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from easy_select2 import select2_modelform

from .models import NewsCategory, NewsItem



class NewsCategoryAdmin(SortableAdmin, PlaceholderAdminMixin, admin.ModelAdmin):

    list_display = ('name', )
    order_by = ('order', )
    prepopulated_fields = {"slug": ("name", )}

    fieldsets = (
        (None, {
            'fields': (
                'name',
                'slug',
                'key_image'
            ),
        }),
    )

admin.site.register(NewsCategory, NewsCategoryAdmin)


class NewsItemAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    form = select2_modelform(NewsItem, attrs={'width': '250px'})
    list_display = ('title', 'start_date', 'announcement', 'published', )
    list_editable = ('announcement', 'published', )
    prepopulated_fields = {"slug": ("title", )}

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'slug',
                'full_title',
                'funding',
                'start_date',
                'categories',
                'related_staff',
                'key_image',
                'key_image_tooltip',
            ),
        }),
    )

admin.site.register(NewsItem, NewsItemAdmin)
