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


class VideoFileSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = Video
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.file == '':
            pass
        else:
            return str(obj.file)

    def get_media_update(self, obj):
        if obj.file == '':
            pass
        else:
            return str(obj.file.date)