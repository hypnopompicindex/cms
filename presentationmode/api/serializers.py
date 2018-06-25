from presentationmode.models import Presentation
from rest_framework import serializers


class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = '__all__'


class PresentationImageOverlaySerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = Presentation
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.image_overlay == '':
            pass
        else:
            return str(obj.image_overlay)

    def get_media_update(self, obj):
        if obj.image_overlay == '':
            pass
        else:
            return str(obj.image_overlay.date)