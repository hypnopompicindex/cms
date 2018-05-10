from globalsettings.models import ContentCard
from rest_framework import viewsets
from globalsettings.api.serializers import ContentCardSerializer


class ContentCardViewSet(viewsets.ModelViewSet):
    queryset = ContentCard.objects.all().order_by('order')
    serializer_class = ContentCardSerializer
