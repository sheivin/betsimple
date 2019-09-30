from django.urls import path

from . import views

app_name = 'bets'
urlpatterns = [
	path('', views.index, name='index'),
	path('competitions', views.competitions, name='competitions'),
	# path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	# path('<int:event_id>/bet/', views.bet, name='bet'),
]