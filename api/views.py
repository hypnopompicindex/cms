from drf_multiple_model.views import ObjectMultipleModelAPIView
from wowmode.api.serializers import VideolistSerializer
from wowmode.models import Videolist
from enticemode.api.serializers import SequenceSerializer
from enticemode.models import Sequence
from mainmenu.api.serializers import ContentGroupSerializer
from mainmenu.models import ContentGroup
from kidszone.api.serializers import VideoSerializer, ThemeSerializer
from kidszone.models import Video, Theme
from presentationmode.api.serializers import PresentationSerializer
from presentationmode.models import Presentation
from globalsettings.api.serializers import ContentStylingSerializer
from globalsettings.models import ContentStyling


class AllAPIView(ObjectMultipleModelAPIView):
    querylist = (
        {'queryset': Videolist.objects.all(), 'serializer_class': VideolistSerializer, 'label': 'Wow Mode',},
        {'queryset': Sequence.objects.all(), 'serializer_class': SequenceSerializer, 'label': 'Entice Mode',},
        {'queryset': ContentGroup.objects.all(), 'serializer_class': ContentGroupSerializer, 'label': 'Main Menu',},
        {'queryset': Theme.objects.all(), 'serializer_class': ThemeSerializer, 'label': 'Kids Zone Themes',},
        {'queryset': Video.objects.all(), 'serializer_class': VideoSerializer, 'label': 'Kids Zone Themes Video',},
        {'queryset': Presentation.objects.all(), 'serializer_class': PresentationSerializer, 'label': 'Presentation Mode',},
        {'queryset': ContentStyling.objects.all(), 'serializer_class': ContentStylingSerializer, 'label': 'Global Settings',},
    )