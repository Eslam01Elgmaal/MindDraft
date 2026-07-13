from django.db import models

# Create your models here.
class Turn(models.TextChoices):
    PLAYER_ONE = "P1", "Player One"
    PLAYER_TWO = "P2", "Player Two"


class GameMode(models.TextChoices):
    SINGLE = "S", "Single"
    LOCAL = "L", "Local"

class Position(models.TextChoices):
    GK = "GK", "GK"
    RB = "RB", "RB"
    CB = "CB", "CB"
    LB = "LB", "LB"
    CDM = "CDM", "CDM"
    CM = "CM", "CM"
    CAM = "CAM", "CAM"
    RW = "RW", "RW"
    ST = "ST", "ST"
    LW = "LW", "LW"

class FootballPlayer(models.Model):
    name = models.CharField( max_length=50)
    position = models.CharField(max_length=3, choices=Position.choices )
    image = models.ImageField(upload_to='players/')

    def __str__(self):
        return self.name

class Game(models.Model):
    player_one_name = models.CharField( max_length= 50)
    player_two_name = models.CharField( max_length= 50)
    game_mode = models.CharField(max_length=1, choices=GameMode.choices )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.player_one_name} vs {self.player_two_name}"

class Pick(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="picks")
    pick_owner = models.CharField(max_length=2, choices=Turn.choices)
    hidden_player = models.ForeignKey(FootballPlayer, on_delete=models.CASCADE, related_name="hidden_picks")
    visible_player = models.ForeignKey(FootballPlayer, on_delete=models.CASCADE, related_name="visible_picks")
    is_visible_selected = models.BooleanField()

    def __str__(self):
        return f"{self.game} - {self.pick_owner}"
    