from globalsettings.models import ContentStyling
from rest_framework import serializers


class ContentStylingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentStyling
        fields = '__all__'
