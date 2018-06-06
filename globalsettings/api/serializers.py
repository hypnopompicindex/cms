from globalsettings.models import ContentStyling, VideoWall
from rest_framework import serializers


class ContentStylingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentStyling
        fields = '__all__'


class VideoWallSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoWall
        fields = '__all__'