# # -*- coding: utf-8 -*-
#
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _




class formDesignerApp(CMSApp):
    name = _('form_designer')
    urls = ['form_designer.urls', ]
    app_name = 'form_designer'


apphook_pool.register(formDesignerApp)
