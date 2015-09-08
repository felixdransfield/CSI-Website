
from cms.models.pluginmodel import CMSPlugin
from adminsortable.models import Sortable
from collections import Counter
from datetime import date
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from filer.fields.image import FilerImageField
from cms.models.fields import PlaceholderField


class NewsManager(models.Manager):

    def get_months(self, category_slug=None, years_only=False, edit_mode=False):

        if edit_mode:
            qs = self
        else:
            qs = self.filter(
                published=True,
                start_date__lte=timezone.now
            )

        if category_slug:
            qs = qs.filter(categories__slug=category_slug)

        dates = qs.values_list('start_date', flat=True)

        if years_only:
            dates = [x.year for x in dates]
        else:
            dates = [(x.year, x.month) for x in dates]
        date_counter = Counter(dates)
        dates = set(dates)
        dates = sorted(dates, reverse=True)

        if years_only:
            return [{
                'date': date(year=year, month=1, day=1),
                'count': date_counter[year]
            } for year in dates]
        else:
            return [{
                'date': date(year=year, month=month, day=1),
                'count': date_counter[year, month]
            } for year, month in dates]


class NewsCategory(Sortable):
    class Meta:
        app_label = 'news'
        verbose_name_plural = 'news categories'

    taints_cache = True

    name = models.CharField('category name',
        blank=False,
        default='',
        help_text=u'Please provide a unique name for this news category.',
        max_length=64,
    )

    slug = models.SlugField('slug',
        blank=False,
        default='',
        help_text='',
        max_length=255,
    )

    info = PlaceholderField('category_info')

    key_image = FilerImageField(
        blank=False,
        help_text=u'Optional. Please supply an image, if one is desired. This '
                  u'will be resized automatically.',
        null=False,
        related_name='category_key_image',
    )


    def get_absolute_url(self):
        return reverse('news:archive', kwargs={'category_slug': self.slug})

    def __unicode__(self):
        return self.name


class NewsItem(models.Model):
    class Meta:
        app_label = 'news'
        ordering = ['-start_date', ]

    taints_cache = True

    title = models.CharField(
        'title',
        blank=False,
        default='',
        help_text=u'Please provide a title for the Research item (usually and acronym',
        max_length=255,
    )

    slug = models.SlugField(
        'slug',
        blank=False,
        default='',
        help_text='the slug that will be the url for this research item',
        max_length=255,
    )

    announcement = models.BooleanField(
        u'announcement?',
        default=False,
        help_text=u'Check this box to display this item in the '
                  u'Announcements box on the front page.',
    )

    announcement_title = models.CharField(
        'announcement title',
        blank=True,
        default='',
        help_text=u'Optional. Alternate title to be used in the '
                  u'Announcements Box on the front page.',
        max_length=255,
    )

    full_title = models.CharField(
        'full_title',
        blank=True,
        default='',
        help_text=u' Please provide the full title for this '
                  u'research item.',
        max_length=555,
    )

    categories = models.ManyToManyField(
        'news.NewsCategory',
        blank=False,
        help_text=u'Please select one or more categories for this news item.',
        related_name='news_items',
    )

    funding = models.CharField(
        'funding',
        blank=True,
        help_text=u'Optional: information on who is funding this research',
        max_length=240,
    )



    published = models.BooleanField(
        'published',
        default=True,
        help_text=u'Check to allow this news post to be publically visible',
    )

    start_date = models.DateField(
        u'research start date',
        blank=False,
        default=timezone.now,
        help_text=u'Please provide the date that this study started '
                  u'the default is the current time '

    )

    mod_date = models.DateTimeField(
        u'modification date',
        auto_now=True,
        editable=False,
    )

    def is_future_publication(self):
        '''
        Returns ``True`` if this news item has a future start_date, else
        ``False``.
        '''
        return bool(self.start_date > timezone.now())

    objects = NewsManager()

    related_staff = models.ManyToManyField(
        'staff.StaffMember',
        blank=True,
        help_text=u'Optional. Please choose zero or more staff related to '
                  u'this item. Selected staff will automatically get a '
                  u'Publication added that references this news item.',
        null=True,
        related_name='news_items',
        verbose_name=u'related staff',
    )

    key_image = FilerImageField(
        blank=True,
        help_text=u'Optional. Please supply an image, if one is desired. This '
                  u'will be resized automatically.',
        null=True,
        related_name='news_key_image',
    )

    key_image_tooltip = models.CharField(
        'key image tooltip',
        blank=True,
        default='',
        help_text='',
        max_length=255,
    )

    news_body = PlaceholderField('news_item_body')

    # def get_staff(self):
    #     return "\n".join([p.related_staff for p in self.related_staff.all()])

    def get_absolute_url(self):
        return reverse('news:news_item_detail', kwargs={'slug': self.slug})

    #
    # Purpose of this save() override:
    # =========================================================================
    # While this is not *required* per-se, it is a nice convenience to already
    # have a Text plugin to work with, since this means all editing can be
    # performed in Content mode and there is no longer the requirement to flip
    # to Structure mode first, just to create the Text plugin in this
    # placeholder.
    #
    def save(self, *args, **kwargs):
        #
        # Do NOT move this import out of this method. Bad things will happen
        # otherwise.
        #
        from cms.api import add_plugin

        if not self.pk:
            super(NewsItem, self).save(*args, **kwargs)
            add_plugin(
                self.news_body,
                'TextPlugin',
                'en',
                body="<p>Placeholder for information about the study/results etc.</p>"
            )
        else:
            super(NewsItem, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title








class RecentNewsPluginModel(CMSPlugin):
    class Meta:
        app_label = 'news'

    taints_cache = True

    max_items = models.PositiveIntegerField('max. number',
        blank=False,
        default=5,
        help_text=u'Please provide the maximum number of items to display (0 means unlimited)',
    )


class NewsArchivePluginModel(CMSPlugin):
    class Meta:
        app_label = 'news'

    taints_cache = True

    show_months = models.BooleanField('show months?',
        default=False,
        help_text=u'Check this option to break the archive down into years and months.',
    )
