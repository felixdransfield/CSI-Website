from django.conf.urls import patterns, url

from views import publications

urlpatterns = [
    # List View
    url(r'^$', 'clippings.views.publications'),

]