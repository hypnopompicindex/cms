from globalsettings.models import ContentStyling, VideoWall
from rest_framework import viewsets
from globalsettings.api.serializers import ContentStylingSerializer, VideoWallSerializer


class ContentStylingViewSet(viewsets.ModelViewSet):
    queryset = ContentStyling.objects.all().order_by('order')
    serializer_class = ContentStylingSerializer


class VideoWallViewSet(viewsets.ModelViewSet):
    queryset = VideoWall.objects.all()
    serializer_class = VideoWallSerializer
