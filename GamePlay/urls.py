from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_game, name="start_game"),

    path("game/<int:game_id>/", views.game_core, name="game_core"),

    path("pick/<int:game_id>/", views.game_pick, name="game_pick"),
]