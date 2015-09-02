from django.shortcuts import render
from models import Clipping
from staff.models import StaffMember



def publications(request):

    return render(request, 'Publications.html',
                  {'publications': Clipping.objects.all,

                   })

