from mainmenu.models import ContentGroup, ContentGallery
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
