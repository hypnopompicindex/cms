from kidszone.models import Video, Theme
from rest_framework import viewsets
from kidszone.api.serializers import VideoSerializer, ThemeSerializer, VideoVideoTimestampSerializer, VideoImageTimestampSerializer, ThemeBackgroundImageTimestampSerializer, ThemeBubbleImageTimestampSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('order')
    serializer_class = VideoSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all().order_by('order')
    serializer_class = ThemeSerializer


class VideoVideoTimestampViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoVideoTimestampSerializer


class VideoImageTimestampViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoImageTimestampSerializer


class ThemeBackgroundImageTimestampViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeBackgroundImageTimestampSerializer


class ThemeBubbleImageTimestampViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeBubbleImageTimestampSerializer
