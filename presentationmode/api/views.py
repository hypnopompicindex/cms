from presentationmode.models import Presentation
from rest_framework import viewsets
from presentationmode.api.serializers import PresentationSerializer


class PresentationViewSet(viewsets.ModelViewSet):
    queryset = Presentation.objects.all().order_by('order')
    serializer_class = PresentationSerializer
