from presentationmode.models import Presentation
from rest_framework import viewsets
from presentationmode.api.serializers import *


class PresentationViewSet(viewsets.ModelViewSet):
    queryset = Presentation.objects.all().order_by('order')
    serializer_class = PresentationSerializer


class PresentationImageOverlayViewSet(viewsets.ModelViewSet):
    queryset = Presentation.objects.all().order_by('order')
    serializer_class = PresentationImageOverlaySerializer
