from django.shortcuts import render
from forms import ParticipationForm
from models import Participation
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.

def new_participant(request):
    if request.POST:
        form = ParticipationForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.date = timezone.now()
            c.save()

            return HttpResponseRedirect('/get-involved/')

    else:
        form = ParticipationForm()

    args = {}

    args['form'] = form


    return render(request, 'new_participant.html', args)