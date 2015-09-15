# -*- coding: utf-8 -*-

from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableTabularInline
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from easy_select2 import select2_modelform
from publications.models import Publication
from news.models import NewsItem
from .models import Seniority, StaffMember


class SeniorityAdmin(admin.ModelAdmin):
	pass

admin.site.register(Seniority, SeniorityAdmin)


class StaffMemberAdmin(PlaceholderAdminMixin, SortableAdmin, admin.ModelAdmin):
	form = select2_modelform(StaffMember, attrs={'width': '250px'})

admin.site.register(StaffMember, StaffMemberAdmin)

