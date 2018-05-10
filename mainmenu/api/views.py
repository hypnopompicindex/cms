from mainmenu.models import ContentGroup
from rest_framework import viewsets
from mainmenu.api.serializers import ContentGroupSerializer


class ContentGroupViewSet(viewsets.ModelViewSet):
    queryset = ContentGroup.objects.all()
    serializer_class = ContentGroupSerializer
