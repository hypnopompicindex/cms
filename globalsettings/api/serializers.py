from globalsettings.models import ContentCard
from rest_framework import serializers


class ContentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCard
        fields = '__all__'
