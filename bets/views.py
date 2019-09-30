from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View, generic
from django.utils import timezone
from django.views.generic.list import ListView

import requests
import json


from .models import *
from .api_util import connect

# Create your views here.

def index(request):
	return HttpResponse("Testing index")

# class CompetitionsView(ListView):
# 	"""
# 	View all competitions
# 	"""
# 	model = Competition
# 	template_name = "competitions.html"

class CompetitionsView(ListView):
	"""
	Displays all the competitions
	"""
	template_name = "competitions.html"
	model = Competition


def competitions(request):
	# url = "http://api.football-data.org/v2/competitions"
	# response = connect(url)

	# competitions_data = response["competitions"]

	# competitions_list = []
	# for competition in competitions_data:
	# 	competitions_list.append(competition["name"])
	# return render(request, 'competitions.html', {'competitions_list': competitions_list})

	return HttpResponse("Building competitions model and adding functionality to view competitions by id.")


class Register(View):
	template_name='bets/register'

	# def form_valid(self, form):

class Fixtures(View):
	template_name = "fixtures.html"
	

# class IndexView(generic.ListView):
	# template_name = 'bets/index.html'
	# context_object_name = 'latest_fixtures_list'

	# def get_queryset(self):
	# 	"""
	# 	Return the last five published bets (not including those
	# 	set to be published in the future).
	# 	"""
	# 	return Event.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# class DetailView(generic.DetailView):
# 	model = Fixture
# 	template_name = 'bets/detail.html'

# class ResultsView(generic.DetailView):
# 	model = Fixture
# 	template_name = 'bets/results.html'

# # def index(request):
# # 	latest_event_list = Event.objects.order_by('-pub_date')[:5]
# # 	template = loader.get_template('bets/index.html')
# # 	context = {
# # 		'latest_event_list': latest_event_list,
# # 	}
# # 	return HttpResponse(template.render(context, request))

# # def detail(request, event_id):
# # 	return HttpResponse("You're looking at event %s." % event_id)

# # def results(request, event_id):
# # 	event = get_object_or_404(Event, pk=event_id)
# # 	return render(request, 'bets/results.html', {'event': event})

# def bet(request, event_id):
# 	event = get_object_or_404(Event, pk=event_id)
# 	try:
# 		selected_bet = event.count_set.get(pk=request.POST['count'])
# 	except (KeyError, Count.DoesNotExist):
# 		return render(request, 'bets/detail.html', {
# 			'event': event,
# 			'error_message': "No bet placed. Don't worry everything's free (for now)!",
# 			})
# 	else:
# 		selected_bet.for_count += 1
# 		selected_bet.save()
# 		return HttpResponseRedirect(reverse('bets:results', args=(event.id,)))
# 	# finally:
# 	# 	pass
# 	# return HttpResponse("You're betting on event %s." % event_id)