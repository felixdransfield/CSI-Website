__author__ = 'felixdransfield'
# # -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _




class PublicationsApp(CMSApp):
    name = _('Publications')
    urls = ['publications.urls', ]
    app_name = 'publications'


apphook_pool.register(PublicationsApp)
