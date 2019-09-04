from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Event

# Create your views here.


def index(request):
	latest_event_list = Event.objects.order_by('-pub_date')[:5]
	template = loader.get_template('bets/index.html')
	context = {
		'latest_event_list': latest_event_list,
	}
	return HttpResponse(template.render(context, request))

def detail(request, event_id):
	return HttpResponse("You're looking at event %s." % event_id)

def results(request, event_id):
	response = "You're looking at bets for event %s."
	return HttpResponse(response % event_id)

def bet(request, event_id):
	return HttpResponse("You're betting on event %s." % event_id)