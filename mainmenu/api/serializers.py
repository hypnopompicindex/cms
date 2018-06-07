from mainmenu.models import ContentGroup, ContentCard, ContentGallery
from rest_framework import serializers


class ContentGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentGallery
        fields = ('title', 'priority', 'gallery_image')


class ContentCardSerializer(serializers.ModelSerializer):
    galleries = ContentGallerySerializer(read_only=True, many=True)

    class Meta:
        model = ContentCard
        fields = ('id', 'title', 'creation_date', 'active', 'priority', 'date_override', 'label', 'content_type', 'invert_content_view', 'text', 'video', 'galleries')


class ContentGroupSerializer(serializers.ModelSerializer):
    card = ContentCardSerializer(read_only=True, many=True)

    class Meta:
        model = ContentGroup
        fields = ('id', 'title', 'active', 'secret', 'lft', 'rght', 'tree_id', 'level', 'parent', 'card')
