# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import PeopleListView, AlumniListView, StaffDetailView


urlpatterns = patterns('',

    # List View
    url(r'^people/$', PeopleListView, name="staffmember_list"),
    url(r'^alumni/$', AlumniListView, name="alumni"),

    #url(r'^(?P<slug>[^/]+)/$', StaffDetailView, name='staffmember_detail'),

    # Detail View
    url(r'^(?P<slug>[^/]+)/$', StaffDetailView.as_view(), name='staffmember_detail'),
)
