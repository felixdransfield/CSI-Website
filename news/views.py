# -*- coding: utf-8 -*-

from datetime import date

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView
from django.views.generic.base import RedirectView
from django.views.generic.dates import ArchiveIndexView
from django.shortcuts import render

from .models import NewsItem, NewsCategory
from staff.models import StaffMember


class NewsItemDetailView(DetailView):
    model = NewsItem
    slug_field = 'slug'

    def get_queryset(self):
        qs = super(NewsItemDetailView, self).get_queryset()

        return qs.filter(published=True, start_date__lte=timezone.now)


    def get_context_data(self, **kwargs):

        context = super(NewsItemDetailView, self).get_context_data(**kwargs)

        related_staff = self.object.related_staff

        context['related_staff'] = related_staff

        # if self.object.start_date > timezone.now():
        #     context['future_publication'] = True

        return context


    def render_to_response(self, context, **response_kwargs):

        #
        # This is just a shim to affect the CMS Toolbar, when present
        #
        if self.request.toolbar:
            menu = self.request.toolbar.get_or_create_menu('news-item-menu', 'News Item')
            menu.add_sideframe_item(_('News Category List'), url=reverse('admin:news_newscategory_changelist'))
            menu.add_modal_item(_('Add new News Category'), url=reverse('admin:news_newscategory_add'))
            menu.add_break()
            menu.add_modal_item(_('Change this News Item'), url=reverse('admin:news_newsitem_change', args=[self.object.id]))
            menu.add_break()
            menu.add_modal_item(_('Add new News Item'), url=reverse('admin:news_newsitem_add'))

        return super(NewsItemDetailView, self).render_to_response(context, **response_kwargs)



class NewsArchiveView(ArchiveIndexView):
    allow_empty = True
    allow_future = True
    date_field = 'start_date'
    model = NewsItem
    paginate_by = 5

    def get_queryset(self):
        qs = super(NewsArchiveView, self).get_queryset()

        if not (self.request.toolbar and self.request.toolbar.edit_mode):
            qs = qs.filter(published=True, start_date__lte=timezone.now)

        category_slug = self.kwargs['category_slug'] if 'category_slug' in self.kwargs else None

        if category_slug:
            qs = qs.filter(categories__slug=category_slug)

        if 'day' in self.kwargs:
            qs = qs.filter(start_date__day=self.kwargs['day'])
        if 'month' in self.kwargs:
            qs = qs.filter(start_date__month=self.kwargs['month'])
        if 'year' in self.kwargs:
            qs = qs.filter(start_date__year=self.kwargs['year'])

        return qs

    def get_context_data(self, **kwargs):
        kwargs['category_slug'] = self.kwargs['category_slug'] if 'category_slug' in self.kwargs else None
        kwargs['day'] = int(self.kwargs.get('day')) if 'day' in self.kwargs else None
        kwargs['month'] = int(self.kwargs.get('month')) if 'month' in self.kwargs else None
        kwargs['year'] = int(self.kwargs.get('year')) if 'year' in self.kwargs else None

        if kwargs['year']:
            kwargs['archive_date'] = date(
                kwargs['year'],
                kwargs['month'] or 1,
                kwargs['day'] or 1
            )

        context = super(NewsArchiveView, self).get_context_data(**kwargs)

        # request = context['request']
        other_params = self.request.GET.copy()
        # Remove the page param, if present.
        if 'page' in other_params:
            other_params.pop('page')
        context['other_params'] = other_params.urlencode()

        return context

    def render_to_response(self, context, **response_kwargs):

        #
        # This is just a shim to affect the CMS Toolbar, when present
        #
        if self.request.toolbar:
            menu = self.request.toolbar.get_or_create_menu('news-list-menu', 'Newsroom')
            menu.add_sideframe_item(_('News Category List'), url=reverse('admin:news_newscategory_changelist'))
            menu.add_modal_item(_('Add new News Category'), url=reverse('admin:news_newscategory_add'))
            menu.add_break()
            menu.add_modal_item(_('Add new News Item'), url=reverse('admin:news_newsitem_add'))

        return super(NewsArchiveView, self).render_to_response(context, **response_kwargs)


def NewsCategoryDetail(request, category_slug):
    categories = NewsCategory.objects.all
    category = NewsCategory.objects.get(slug=category_slug)
    items = NewsItem.objects.filter(categories__id=category.id)



    return render(request, 'newscategory_detail.html',{'catagories':categories,
                                                       'category': category,
                                                       'items': items,
                                                    })


# def NewsItemDetailView2(request):
#     return render(request, 'newsitem_detail.html', {'item': NewsItem.objects.get(slug=item_slug)})