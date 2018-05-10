from presentationmode.models import Presentation
from rest_framework import serializers


class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = '__all__'
