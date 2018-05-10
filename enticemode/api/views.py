from enticemode.models import Sequence
from rest_framework import viewsets
from enticemode.api.serializers import SequenceSerializer


class SequenceViewSet(viewsets.ModelViewSet):
    queryset = Sequence.objects.all().order_by('order')
    serializer_class = SequenceSerializer
