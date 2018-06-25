from enticemode.models import Sequence
from rest_framework import serializers


class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequence
        fields = '__all__'


class SequenceIntroVideoSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = Sequence
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.intro_video == '':
            pass
        else:
            return str(obj.intro_video)

    def get_media_update(self, obj):
        if obj.intro_video == '':
            pass
        else:
            return str(obj.intro_video.date)


class SequenceOutroVideoSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = Sequence
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.outro_video == '':
            pass
        else:
            return str(obj.intro_video)

    def get_media_update(self, obj):
        if obj.outro_video == '':
            pass
        else:
            return str(obj.outro_video.date)


class SequenceTouchIndicatorVideoSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = Sequence
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.touch_indicator_video == '':
            pass
        else:
            return str(obj.touch_indicator_video)

    def get_media_update(self, obj):
        if obj.touch_indicator_video == '':
            pass
        else:
            return str(obj.touch_indicator_video.date)


class SequenceBackgroundVignetteVideoSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = Sequence
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.background_vignette_video == '':
            pass
        else:
            return str(obj.background_vignette_video)

    def get_media_update(self, obj):
        if obj.background_vignette_video == '':
            pass
        else:
            return str(obj.background_vignette_video.date)
