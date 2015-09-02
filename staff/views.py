# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from models import StaffMember
from django.shortcuts import render




def PeopleListView(request):
    academic_staff = StaffMember.objects.filter(seniority_id=4 or 3, is_current=True)
    phd_students = StaffMember.objects.filter(seniority_id=1, is_current=True)
    research_assistants = StaffMember.objects.filter(seniority_id=3, is_current=True)
    people_title = True

    return render(request, 'staffmember_list.html', {
                                                     'people_title': people_title,
                                                     'academic_staff':academic_staff,
                                                     'phd_students': phd_students,
                                                     'research_assistants': research_assistants})

def AlumniListView(request):
    object_list = StaffMember.objects.filter(is_current=False)
    people_title = False

    return render(request, 'staffmember_list.html', {'object_list': object_list,
                                                     'people_title': people_title})



class StaffDetailView(DetailView):
    model = StaffMember
    context_object_name = 'staff'

    def render_to_response(self, context, **response_kwargs):
        # Shim to affect the CMS Toolbar only
        if self.request.toolbar and self.request.toolbar.edit_mode:
            menu = self.request.toolbar.get_or_create_menu('staff-member-menu', self.object.full_name)
            menu.add_modal_item('Edit %s' % self.object.full_name, url=reverse('admin:staff_staffmember_change', args=[self.object.id]), )

            menu.add_break()


            menu.add_modal_item('Attach New Clipping',
                url="%s" % (reverse('admin:clippings_clipping_add'), )
            )


            menu.add_modal_item('Attach New Clipping',
                url="%s?staff=%d" % (
                    reverse('admin:clippings_clipping_add'),
                    self.object.id,
                )
            )


        return super(StaffDetailView, self).render_to_response(context, **response_kwargs)
