# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break, SubMenu
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK


@toolbar_pool.register
class PublicationsToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Apps'))

        position = admin_menu.get_alphabetical_insert_position(
            _('Publications'),
            SubMenu
        )

        if not position:
            position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK) + 1
            # Despite what it appears, this will actually come after the first
            # custom menu.
            admin_menu.add_break('custom-break', position=position)

        menu = admin_menu.get_or_create_menu('publications-menu', _('Publications ...'), position=position)

        url = reverse('admin:publications_publication_changelist')
        menu.add_sideframe_item(_('Publication List'), url=url)

        url = reverse('admin:publications_publication_add')
        menu.add_modal_item(_('Add New Publication'), url=url)

        url = reverse('admin:publications_publication_import_bibtex')
        menu.add_modal_item(_('Import BibTex'), url=url)


