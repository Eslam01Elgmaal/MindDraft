from django.shortcuts import render
from .models import Game, FootballPlayer, Pick, GameMode

# Create your views here.

def start_game(request):

    if request.method == "POST":

        player_one_name = request.POST.get("player_one_name")
        game_mode = request.POST.get("game_mode")

        if game_mode == GameMode.SINGLE:
            player_two_name = "Computer"

        else:
            player_two_name = request.POST.get("player_two_name")

        game = Game.objects.create(
            player_one_name=player_one_name,
            player_two_name=player_two_name,
            game_mode=game_mode,
        )

        return redirect("round", game.id)

    return render(request, "GamePlay/start_game.html")





def game_core():
    pass


def game_pick():
    pass


