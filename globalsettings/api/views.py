from globalsettings.models import ContentStyling
from rest_framework import viewsets
from globalsettings.api.serializers import ContentStylingSerializer


class ContentStylingViewSet(viewsets.ModelViewSet):
    queryset = ContentStyling.objects.all().order_by('order')
    serializer_class = ContentStylingSerializer
