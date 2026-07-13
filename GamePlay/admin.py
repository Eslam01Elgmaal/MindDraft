from django.contrib import admin
from .models import FootballPlayer, Game, Pick




@admin.register(FootballPlayer)

class FootballPlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "position")

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "player_one_name",
        "player_two_name",
        "game_mode",
        "created_at",
    )

@admin.register(Pick)
class PickAdmin(admin.ModelAdmin):
    list_display = (
        "game",
        "pick_owner",
        "visible_player",
        "hidden_player",
        "is_visible_selected",
    )
