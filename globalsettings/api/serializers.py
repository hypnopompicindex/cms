from globalsettings.models import ContentStyling, VideoWall, Publish
from rest_framework import serializers


class ContentStylingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentStyling
        fields = '__all__'


class VideoWallSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoWall
        fields = '__all__'


class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'


class ContentStylingImageSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = ContentStyling
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.image == '':
            pass
        else:
            return str(obj.image)

    def get_media_update(self, obj):
        if obj.image == '':
            pass
        else:
            return str(obj.image.date)
