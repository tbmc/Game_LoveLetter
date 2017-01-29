from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = User
        fields = ("url", "username", "email", "groups")

