from rest_framework import serializers
from wowmode.models import Videolist, Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'order', 'file', 'thumbnail')


class VideolistSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(read_only=True, many=True)

    class Meta:
        model = Videolist
        fields = ('id', 'title', 'order', 'active', 'start_date', 'end_date', 'videos')
