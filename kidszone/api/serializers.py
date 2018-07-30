from kidszone.models import Video, Theme
from rest_framework import serializers


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'


class VideoVideoTimestampSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = Video
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.video == '':
            pass
        else:
            return str(obj.video)

    def get_media_update(self, obj):
        if obj.video == '':
            pass
        else:
            return str(obj.video.date)


class VideoImageTimestampSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = Video
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


class ThemeBackgroundImageTimestampSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = Theme
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.background_image == '':
            pass
        else:
            return str(obj.background_image)

    def get_media_update(self, obj):
        if obj.background_image == '':
            pass
        else:
            return str(obj.background_image.date)


class ThemeBubbleImageTimestampSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = Theme
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.bubble_image_1 == '':
            pass
        else:
            return str(obj.bubble_image_1)

    def get_media_update(self, obj):
        if obj.bubble_image_1 == '':
            pass
        else:
            return str(obj.bubble_image_1.date)


class ThemeBubbleImage2TimestampSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = Theme
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.bubble_image_2 == '':
            pass
        else:
            return str(obj.bubble_image_2)

    def get_media_update(self, obj):
        if obj.bubble_image_2 == '':
            pass
        else:
            return str(obj.bubble_image_2.date)


class ThemeBubbleImage3TimestampSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = Theme
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.bubble_image_3 == '':
            pass
        else:
            return str(obj.bubble_image_3)

    def get_media_update(self, obj):
        if obj.bubble_image_3 == '':
            pass
        else:
            return str(obj.bubble_image_3.date)
