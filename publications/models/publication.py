# -*- coding: utf-8 -*-
from django.db import models
from filer.fields.file import FilerFileField
from django.utils import timezone
from adminsortable.models import Sortable
from django.db.models import F
import csv



class Publication(Sortable):
    class Meta(Sortable.Meta):
        app_label = 'publications'

    taints_cache = True

    staff = models.ForeignKey('staff.StaffMember',
        blank=False,
        default=None,
        help_text=u'Required. To whom is this publication connected?',
        null=False,
        related_name='publications',
    )

    title = models.CharField('title',
        blank=True,
        default='',
        help_text=u'Please provide a title for this publication.',
        max_length=255,
    )

    pub_date = models.DateField('date of publication', default=timezone.now, blank=True)

    source = models.CharField('source',
        blank=True,
        default='',
        help_text=u'Please provide a the name of the journal it was published in.',
        max_length=255,
    )

    download = FilerFileField(
        blank=True,
        null=True,
        help_text=u'Provide a file download. this will override an external link if given.',
    )

    news_item = models.ForeignKey('news.NewsItem',
        blank=True,
        default=None,
        help_text=u'Select a Research Item. This overrides external links.',
        null=True,
    )

    external_link = models.CharField(u'external link',
        blank=True,
        default='',
        help_text=u'Provide an external link to the publication.',
        max_length=2048,
    )



    def get_type(self):
        '''Returns the type of publication this is'''
        if self.download:
            return 'file download'
        elif self.news_item:
            return 'research post'
        elif self.external_link:
            return 'external link'
        else:
            return 'unknown'

    def get_absolute_url(self):
        if self.download:
            return self.download.url
        elif self.news_item:
            return self.news_item.get_absolute_url()
        elif self.external_link:
            return self.external_link
        return None

    def get_target(self):
        if self.download:
            return '_blank'
        elif self.news_item:
            return ''
        elif self.external_link:
            return '_blank'
        return None

    get_type.short_description = 'publication type'


    def save(self, **kwargs):
        from django.utils.text import Truncator
        '''
        Automatically set an appropriate title, depending on the type of media
        selected. Also, new items are at the top of the publications list.
        '''

        is_new = (not self.id)

        if not self.title:
            if self.download:
                self.title = os.path.basename(self.download.file.name)
            elif self.news_item:
                self.title = self.news_item.headline
            elif self.external_link:
                self.title = self.external_link
            else:
                self.title = 'Untitled Publication'

        self.title = Truncator(self.title).chars(252, truncate='...')

        super(Publication, self).save(**kwargs)

        if is_new:
            # We need to push all the other publications "down" one...
            Publication.objects.exclude(id=self.id).update(order=F('order') + 1)
            # OK, there is now 'room' for this entry at an order of 2.
            Publication.objects.filter(id=self.id).update(order=2)



    def __unicode__(self):
        return self.title


#
# NOTE: A research item can "point to" any number of staff members, but we'd like
# the staff members to decide whether that research item will appear on their
# pages. To facilitate this, when we point to a staff member from a research item,
# we'll automatically create a separate, but reciprocal relationship from the
# Staff member to the research Item (via a Clipping object), but it is not the
# same relationship, and one or the other can then be deleted without
# affecting the other.
#
# The signal sender is located in apps.research.models.research_item
# If this note is updated, please update the same note there.
#
def link_staff_to_news_item(sender, instance, action, pk_set, **kwargs):
    from staff.models import StaffMember

    if action == 'post_add':
        for staff in StaffMember.objects.filter(pk__in=pk_set):
            if Publication.objects.filter(staff=staff, external_link='', news_item=instance).count() == 0:
                #
                # OK, looks like staff doesn't already have this as a
                # publication, so create one.
                #

                # print('Creating Publication for %s ...' % staff.full_name)
                publication = Publication()
                publication.staff = staff
                publication.news_item = instance
                publication.save()

# Listen for signals from ResearchItem.related_staff M2M changes
#m2m_changed.connect(link_staff_to_new_item, sender=NewsItem.related_staff.through)
