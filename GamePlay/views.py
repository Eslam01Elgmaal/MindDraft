from django.shortcuts import render
from random import sample
from .models import Game, FootballPlayer, Pick, GameMode, Turn
from django.shortcuts import get_object_or_404, redirect, render

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

        return redirect("game_core", game.id)

    return render(request, "GamePlay/start_game.html")

POSITIONS = [
    "GK",
    "RB",
    "CB",
    "CB",
    "LB",
    "CDM",
    "CM",
    "CAM",
    "RW",
    "ST",
    "LW",
]

TURN = [
    Turn.PLAYER_ONE,
    Turn.PLAYER_TWO,
]
def game_core(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    pick_count = game.picks.count()

    if pick_count == len(POSITIONS):
        return redirect("game_pick", game.id)

    current_position = POSITIONS[pick_count]
    current_turn = TURN[pick_count % 2]

    if current_turn == Turn.PLAYER_ONE:
        current_player = game.player_one_name
    else:
        if game.game_mode == GameMode.SINGLE:
            current_player = "Computer"
        else:
            current_player = game.player_two_name

    if request.method == "POST":

        visible_player = FootballPlayer.objects.get(
            id=request.POST.get("visible_player_id")
        )

        hidden_player = FootballPlayer.objects.get(
            id=request.POST.get("hidden_player_id")
        )

        is_visible_selected = request.POST.get("choice") == "visible"

        Pick.objects.create(
            game=game,
            pick_owner=current_turn,
            visible_player=visible_player,
            hidden_player=hidden_player,
            is_visible_selected=is_visible_selected,
        )

        if game.picks.count() == len(POSITIONS):
            return redirect("game_pick", game.id)

        return redirect("game_core", game.id)

   
    used_players = []

    for pick in game.picks.all():
        used_players.append(pick.visible_player.id)
        used_players.append(pick.hidden_player.id)

  
    players = list(
        FootballPlayer.objects.filter(
            position=current_position
        ).exclude(
            id__in=used_players
        )
    )

    visible_player, hidden_player = sample(players, 2)

    context = {
        "game": game,
        "position": current_position,
        "current_player": current_player,
        "visible_player": visible_player,
        "hidden_player": hidden_player,
    }

    return render(request, "GamePlay/round.html", context)
    
    



def game_pick(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    player_one_team = []
    player_two_team = []

    for pick in game.picks.all():

        
            
        if pick.is_visible_selected:

            selected_player = pick.visible_player
            other_player = pick.hidden_player

        else:

            selected_player = pick.hidden_player
            other_player = pick.visible_player
       

        if pick.pick_owner == Turn.PLAYER_ONE:
            player_one_team.append(selected_player)
            player_two_team.append(other_player)

        else:

            player_two_team.append(selected_player)
            player_one_team.append(other_player)

    context = {
        "game": game,
        "player_one_team": player_one_team,
        "player_two_team": player_two_team,
    }

    return render(request, "GamePlay/result.html", context)


