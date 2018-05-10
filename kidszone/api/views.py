from kidszone.models import Video, Theme
from rest_framework import viewsets
from kidszone.api.serializers import VideoSerializer, ThemeSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('order')
    serializer_class = VideoSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all().order_by('order')
    serializer_class = ThemeSerializer