from django.urls import path # type: ignore
from . import views

#TEMPLATE TAGGING
app_name = 'game'

urlpatterns = [
    path('', views.game_home, name='game_home'),
    path('play/', views.game_play, name='game_play'),
    path('save_score/', views.save_score, name='save_score'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
