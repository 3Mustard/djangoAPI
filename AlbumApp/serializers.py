from rest_framework import serializers
from AlbumApp.models import Albums, Groups

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = ('AlbumId', 'AlbumName', 'Group', 'DateAdded', 'PhotoFileName')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('GroupId', 'GroupName', 'PhotoFileName')