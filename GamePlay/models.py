from django.db import models

# Create your models here.

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
    imge = models.ImageField(upload_to='players/')

    def __str__(self):
        return self.name

class Game(models.Model):
    pass


class Pick(models.Model):
    pass