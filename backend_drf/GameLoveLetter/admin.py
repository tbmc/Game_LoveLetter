# Register your models here.

from django.contrib import admin
from django.db import models
from .models import *


r = admin.site.register

r(Player)
r(CardPacket)
r(Card)
r(Game)
r(PlayerInGame)


