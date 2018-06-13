from mainmenu.models import ContentGroup, ContentCard, ContentGallery, ContentGroupCard, ContentLabel
from rest_framework import serializers


class ContentGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentGallery
        fields = ('title', 'priority', 'gallery_image')


class ContentLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentLabel
        fields = ('id', 'label')


class ContentCardSerializer(serializers.ModelSerializer):
    galleries = ContentGallerySerializer(read_only=True, many=True)

    class Meta:
        model = ContentCard
        fields = ('id', 'title', 'creation_date', 'active', 'date_override', 'content_type', 'invert_content_view', 'text_header', 'text', 'video', 'text_position', 'gradient_overlay', 'galleries')


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
        fields = ('id', 'title', 'active', 'secret', 'lft', 'rght', 'tree_id', 'level', 'parent', 'card', 'content_group')

