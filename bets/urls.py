from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:event_id>/', views.detail, name='detail'),
	path('<int:event_id>/results/', views.results, name='results'),
	path('<int:event_id>/bet/', views.bet, name='bet'),
]