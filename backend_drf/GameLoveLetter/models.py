from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


CARD_LIST = [
    {
        "name": "Garde",
    },
    {
        "name": "Prêtre",
    },
    {
        "name": "Baron",
    },
    {
        "name": "Servante",
    },
    {
        "name": "Prince",
    },
    {
        "name": "Roi",
    },
    {
        "name": "Comtesse",
    },
    {
        "name": "Princesse",
    }
]
CARDS_TUPLES = [(i, CARD_LIST[i]) for i in range(len(CARD_LIST))]


class CardPacket(models.Model):
    pass


class Card(models.Model):
    card = models.IntegerField(choices=CARDS_TUPLES, default=0)
    card_packet = models.ForeignKey(CardPacket, on_delete=models.CASCADE)


class Game(models.Model):
    card_packet = models.ForeignKey(CardPacket, on_delete=models.CASCADE)


class PlayerInGame(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


