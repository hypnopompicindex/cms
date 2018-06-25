from mainmenu.models import ContentGroup, ContentGallery, ContentCard
from rest_framework import viewsets
from mainmenu.api.serializers import *


class ContentGroupViewSet(viewsets.ModelViewSet):
    queryset = ContentGroup.objects.all()
    serializer_class = ContentGroupSerializer


class ContentGalleryViewSet(viewsets.ModelViewSet):
    queryset = ContentGallery.objects.all()
    serializer_class = ContentGalleryImageSerializer


class ContentGroupButtonImageViewSet(viewsets.ModelViewSet):
    queryset = ContentGroup.objects.all()
    serializer_class = ContentGroupButtonImageSerializer


class ContentCardVideoViewSet(viewsets.ModelViewSet):
    queryset = ContentCard.objects.all()
    serializer_class = ContentCardVideoSerializer


class ContentCardButtonImageViewSet(viewsets.ModelViewSet):
    queryset = ContentCard.objects.all()
    serializer_class = ContentCardButtonImageSerializer


class ContentCardGradientOverlayViewSet(viewsets.ModelViewSet):
    queryset = ContentCard.objects.all()
    serializer_class = ContentCardGradientOverlaySerializer