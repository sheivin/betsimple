from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Event, Count

# Create your views here.


class IndexView(generic.ListView):
	template_name = 'bets/index.html'
	context_object_name = 'latest_event_list'

	def get_queryset(self):
		"""
		Return the last five published bets (not including those
		set to be published in the future).
		"""
		return Event.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Event
	template_name = 'bets/detail.html'

class ResultsView(generic.DetailView):
	model = Event
	template_name = 'bets/results.html'

# def index(request):
# 	latest_event_list = Event.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('bets/index.html')
# 	context = {
# 		'latest_event_list': latest_event_list,
# 	}
# 	return HttpResponse(template.render(context, request))

# def detail(request, event_id):
# 	return HttpResponse("You're looking at event %s." % event_id)

# def results(request, event_id):
# 	event = get_object_or_404(Event, pk=event_id)
# 	return render(request, 'bets/results.html', {'event': event})

def bet(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	try:
		selected_bet = event.count_set.get(pk=request.POST['count'])
	except (KeyError, Count.DoesNotExist):
		return render(request, 'bets/detail.html', {
			'event': event,
			'error_message': "No bet placed. Don't worry everything's free (for now)!",
			})
	else:
		selected_bet.for_count += 1
		selected_bet.save()
		return HttpResponseRedirect(reverse('bets:results', args=(event.id,)))
	# finally:
	# 	pass
	# return HttpResponse("You're betting on event %s." % event_id)