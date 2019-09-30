import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Competition(models.Model):
	"""
	Model to represent a football league (competition)
	"""
	api_id = models.IntegerField()
	name = models.CharField(max_length=256)
	code = models.CharField(max_length=12)
	current_season_year = models.IntegerField()
	number_of_teams = models.IntegerField()
	number_of_matchdays = models.IntegerField()
	current_matchday = models.IntegerField()

	def __str__(self):
		return self.name

class Team(models.Model):
	"""
	Model to represent a football league team
	"""
	name = models.CharField(max_length=256)
	short_name = models.CharField(max_length=128)
	code = models.CharField(max_length=12, null=True)
	crest_url = models.CharField(max_length=256)
	competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.name

# Represent possible fixture status as tuple of tuple (alternate: enum)
STATUS = (
	(1, 'SCHEDULED'),
	(2, 'FINISHED'),
	(3, 'PLAYING')
)

class Fixture(models.Model):
	"""
	Model to represent a football league fixture
	"""
	home_team = models.ForeignKey(Team, related_name='homeTeam', on_delete=models.SET_NULL, null=True)
	away_team = models.ForeignKey(Team, related_name='awayTeam', on_delete=models.SET_NULL, null=True)
	competition = models.ForeignKey(Competition, related_name='competition', on_delete=models.CASCADE)
	matchday = models.IntegerField()
	date = models.DateTimeField()
	status = models.IntegerField(choices=STATUS, default=1)

	def __str__(self):
		return str(self.home_team.name + " - " + self.away_team.name)


# Represent possible bet outcomes
BET_OUTCOMES = (
	(0, 'LOST'),
	(1, 'WON'),
	(2, 'PENDING')
)

# Represent possible bet choices
BET_CHOICES = (
	(0, 0),
	(1, 1),
	(2, 2)
)



class Bet(models.Model):
	"""
	Model to represent a bet. Currently supporting football competitions
	"""
	bet_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	fixture = models.ForeignKey(Fixture, related_name='fixture', on_delete=models.CASCADE)
	bet_amount = models.DecimalField(max_digits=6, decimal_places=2)
	bet_choice = models.IntegerField(choices=BET_CHOICES)
	bet_outcome = models.IntegerField(choices=BET_OUTCOMES, default=2, blank=True)


