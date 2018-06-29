from globalsettings.models import ContentStyling, VideoWall, Publish
from rest_framework import viewsets
from globalsettings.api.serializers import *


class ContentStylingViewSet(viewsets.ModelViewSet):
    queryset = ContentStyling.objects.all().order_by('order')
    serializer_class = ContentStylingSerializer


class VideoWallViewSet(viewsets.ModelViewSet):
    queryset = VideoWall.objects.all()
    serializer_class = VideoWallSerializer


class PublishWallViewSet(viewsets.ModelViewSet):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer


class ContentStylingImageViewSet(viewsets.ModelViewSet):
    queryset = ContentStyling.objects.all()
    serializer_class = ContentStylingImageSerializer
