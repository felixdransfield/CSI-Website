# # -*- coding: utf-8 -*-
#
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _




class ClippingsApp(CMSApp):
    name = _('Clippings')
    urls = ['clippings.urls', ]
    app_name = 'clippings'


apphook_pool.register(ClippingsApp)
