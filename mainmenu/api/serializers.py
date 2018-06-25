from mainmenu.models import ContentGroup, ContentCard, ContentGallery, ContentGroupCard, ContentLabel
from rest_framework import serializers


class ContentGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentGallery
        fields = ('title', 'priority', 'gallery_image')


class ContentGalleryImageSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField('get_media_path')
    media_timestamp = serializers.SerializerMethodField('get_media_update')

    class Meta:
        model = ContentGallery
        fields = ('media', 'media_timestamp')

    def get_media_path(self, obj):
        if obj.gallery_image == '':
            pass
        else:
            return str(obj.gallery_image)

    def get_media_update(self, obj):
        if obj.gallery_image == '':
            pass
        else:
            return str(obj.gallery_image.date)


class ContentLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentLabel
        fields = ('id', 'label')


class ContentCardSerializer(serializers.ModelSerializer):
    galleries = ContentGallerySerializer(read_only=True, many=True)

    class Meta:
        model = ContentCard
        fields = ('id', 'title', 'button_image', 'creation_date', 'active', 'date_override', 'content_type', 'invert_content_view', 'text_header', 'text', 'video', 'text_position', 'gradient_overlay', 'galleries')


class ContentGroupCardSerializer(serializers.ModelSerializer):
    card_model = ContentCardSerializer(read_only=True,)
    label = ContentLabelSerializer(read_only=True, many=True)

    class Meta:
        model = ContentGroupCard
        fields = ('id', 'content_card', 'priority', 'label', 'card_model')
        depth = 2


class ContentGroupSerializer(serializers.ModelSerializer):
    card = ContentCardSerializer(read_only=True, many=True)
    content_group = ContentGroupCardSerializer(source='contentgroupcard_set', many=True)

    class Meta:
        model = ContentGroup
        fields = ('id', 'title', 'button_image', 'active', 'secret', 'lft', 'rght', 'tree_id', 'level', 'parent',  'content_group', 'card')


class ContentGroupButtonImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentGroup
        fields = ('media', 'media_timestamp')
