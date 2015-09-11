from django.shortcuts import render, render_to_response, RequestContext
from models import Publication
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def publications(request):

    return render(request, 'publications.html',
                  {'publications': Publication.objects.all,

                   })


