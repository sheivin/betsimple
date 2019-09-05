import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Event

# Create your tests here.

class EventModelTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() returns False for events whose pub_date is
		in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_event = Event(pub_date=time)
		self.assertIs(future_event.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		"""
		was_published_recently() returns False for events whose pub_date is
		older than 1 day.
		"""
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_event = Event(pub_date=time)
		self.assertIs(old_event.was_published_recently(), False)

	def test_was_published_recently_with_recent_questin(self):
		"""
		was_published_recently() returns True for events whose pub_date is
		within the last day.
		"""
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_event = Event(pub_date=time)
		self.assertIs(recent_event.was_published_recently(), True)


def create_event(event_text, days):
	"""
	Create an event with given 'event_text' and publish the given number
	of 'days' offset to now (negative for events published in the past,
	positive for questions that have yet to be published).
	"""
	time = timezone.now() + datetime.timedelta(days=days)
	return Event.objects.create(event_text=event_text, pub_date=time)

class QuestionIndexViewTests(TestCase):

	def test_no_events(self):
		"""
		If no events exist, an appropriate message is displayed.
		"""
		response = self.client.get(reverse('bets:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No bets are available.")
		self.assertQuerysetEqual(response.context['latest_event_list'], [])

	def test_past_event(self):
		"""
		Events with a pub_date in the past are displayed on the index page
		"""
		create_event(event_text="Past event.", days=-30)
		response = self.client.get(reverse('bets:index'))
		self.assertQuerysetEqual(response.context['latest_event_list'],
			['<Event: Past event.>']
		)

	def test_future_event(self):
		"""
		Events with a pub_date in the future aren't displayed on the index page
		"""
		create_event(event_text="Future question.", days=30)
		response = self.client.get(reverse('bets:index'))
		self.assertContains(response, "No bets are available.")
		self.assertQuerysetEqual(response.context['latest_event_list'], [])

	def test_future_event_and_past_event(self):
		"""
		Even if past and future events exist, only past are displayed.
		"""
		create_event(event_text="Past event.", days=-30)
		create_event(event_text="Future event.", days=30)
		response = self.client.get(reverse('bets:index'))
		self.assertQuerysetEqual(response.context['latest_event_list'],
			['<Event: Past event.>']
		)

	def test_two_past_events(self):
		"""
		The events index page may display multiple questions.
		"""
		create_event(event_text="Past event 1.", days=-30)
		create_event(event_text="Past event 2.", days=-5)
		response = self.client.get(reverse('bets:index'))
		self.assertQuerysetEqual(
			response.context['latest_event_list'],
			['<Event: Past event 2.>', '<Event: Past event 1.>']
		)

