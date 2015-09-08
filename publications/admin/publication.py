# -*- coding: utf-8 -*-

from django.contrib import admin

from easy_select2 import select2_modelform
from adminsortable.admin import SortableAdmin
#from ..forms import DataInput
from ..models import Publication

class PublicationAdmin(SortableAdmin):
    form = select2_modelform(Publication, attrs={'width': '250px'})
    list_display = ('staff', 'title', 'get_type', )
    list_display_links = ('staff', 'title', )
    readonly_fields= ('get_type', )

    fieldsets = (
        (None, {
            'fields': (
                'staff',
                'title',
                'source',
                'pub_date',
                'download',
                'news_item',
                'external_link',
            ),
        }),
    )

# class DataAdmin(admin.ModelAdmin):
#     list_display = ("staff",)
#     fieldsets = (
#         (None, {
#             'fields': (
#                 'staff',
#                 'file',
#
#             ),
#         }),
#     )
#     form = DataInput




admin.site.register(Publication, PublicationAdmin)
