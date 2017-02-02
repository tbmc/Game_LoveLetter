from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from . import serializers
from GameLoveLetter.models import Player

class UserViewSet(viewsets.ModelViewSet):
    """
   API endpoint that allows users to be viewed or edited.
   """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by("id")
    serializer_class = serializers.PlayerSerializer

