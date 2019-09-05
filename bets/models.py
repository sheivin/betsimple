import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


## Event model
class Event(models.Model):
	event_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.event_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

## Count model
class Count(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	for_count = models.IntegerField(default=0)
	against_count = models.IntegerField(default=0)
