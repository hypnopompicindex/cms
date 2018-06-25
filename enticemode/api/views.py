from enticemode.models import Sequence
from rest_framework import viewsets
from enticemode.api.serializers import *


class SequenceViewSet(viewsets.ModelViewSet):
    queryset = Sequence.objects.all().order_by('order')
    serializer_class = SequenceSerializer


class SequenceIntroVideoViewSet(viewsets.ModelViewSet):
    queryset = Sequence.objects.all()
    serializer_class = SequenceIntroVideoSerializer


class SequenceOutroVideoViewSet(viewsets.ModelViewSet):
    queryset = Sequence.objects.all()
    serializer_class = SequenceOutroVideoSerializer


class SequenceTouchIndicatorVideoViewSet(viewsets.ModelViewSet):
    queryset = Sequence.objects.all()
    serializer_class = SequenceTouchIndicatorVideoSerializer


class SequenceBackgroundVignetteVideoViewSet(viewsets.ModelViewSet):
    queryset = Sequence.objects.all()
    serializer_class = SequenceBackgroundVignetteVideoSerializer

