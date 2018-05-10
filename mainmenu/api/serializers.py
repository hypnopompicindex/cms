from mainmenu.models import ContentGroup, ContentCard
from rest_framework import serializers
from taggit.models import Tag


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class ContentCardSerializer(serializers.ModelSerializer):
    tags = TagListSerializer(read_only=True, many=True)

    class Meta:
        model = ContentCard
        fields = ('id', 'title', 'thumbnail', 'priority', 'date_override', 'group', 'tags')


class ContentGroupSerializer(serializers.ModelSerializer):
    items = ContentCardSerializer(read_only=True, many=True)

    class Meta:
        model = ContentGroup
        fields = '__all__'
