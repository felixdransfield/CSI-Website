from django.conf.urls import url

urlpatterns = [
    url(r'^get-involved/$', 'participation.views.new_participant'),
]