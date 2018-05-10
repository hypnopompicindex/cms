from wowmode.models import Videolist, Video
from rest_framework import viewsets
from wowmode.api.serializers import VideolistSerializer, VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('order')
    serializer_class = VideoSerializer


class VideolistViewSet(viewsets.ModelViewSet):
    queryset = Videolist.objects.all().order_by('order')
    serializer_class = VideolistSerializer
