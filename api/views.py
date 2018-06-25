from drf_multiple_model.views import ObjectMultipleModelAPIView, FlatMultipleModelAPIView
from wowmode.api.serializers import VideolistSerializer
from wowmode.models import Videolist
from enticemode.api.serializers import SequenceSerializer
from enticemode.models import Sequence
from mainmenu.api.serializers import ContentGroupSerializer
from mainmenu.models import ContentGroup
from kidszone.api.serializers import VideoSerializer, ThemeSerializer, VideoVideoTimestampSerializer, VideoImageTimestampSerializer, ThemeBackgroundImageTimestampSerializer, ThemeBubbleImageTimestampSerializer
from kidszone.models import Video, Theme
from presentationmode.api.serializers import PresentationSerializer
from presentationmode.models import Presentation
from globalsettings.api.serializers import ContentStylingSerializer, VideoWallSerializer
from globalsettings.models import ContentStyling, VideoWall


class AllAPIView(ObjectMultipleModelAPIView):
    querylist = (
        {'queryset': Videolist.objects.all(), 'serializer_class': VideolistSerializer, 'label': 'Wow Mode',},
        {'queryset': Sequence.objects.all(), 'serializer_class': SequenceSerializer, 'label': 'Entice Mode',},
        {'queryset': ContentGroup.objects.all(), 'serializer_class': ContentGroupSerializer, 'label': 'Main Menu',},
        {'queryset': Theme.objects.all(), 'serializer_class': ThemeSerializer, 'label': 'Kids Zone Themes',},
        {'queryset': Video.objects.all(), 'serializer_class': VideoSerializer, 'label': 'Kids Zone Themes Video',},
        {'queryset': Presentation.objects.all(), 'serializer_class': PresentationSerializer, 'label': 'Presentation Mode',},
        {'queryset': ContentStyling.objects.all(), 'serializer_class': ContentStylingSerializer,
         'label': 'Content Styling',},
        {'queryset': VideoWall.objects.all(), 'serializer_class': VideoWallSerializer,
         'label': 'Video Wall',},
        {'queryset': VideoWall.objects.all(), 'serializer_class': VideoWallSerializer,
         'label': 'Video Wall', },
    )


class AllMediaView(FlatMultipleModelAPIView):
    add_model_type = True

    querylist = (
        {'queryset': Video.objects.all().distinct(), 'serializer_class': VideoVideoTimestampSerializer,
         'label': 'Kids Zone Video Video Media', },
        {'queryset': Video.objects.all().distinct(), 'serializer_class': VideoImageTimestampSerializer,
         'label': 'Kids Zone Video Image Media', },
        {'queryset': Theme.objects.all().distinct(), 'serializer_class': ThemeBackgroundImageTimestampSerializer,
         'label': 'Kids Zone Theme Background Image Media', },
        {'queryset': Theme.objects.all().distinct(), 'serializer_class': ThemeBubbleImageTimestampSerializer,
         'label': 'Kids Zone Theme Bubble Image Media', },
    )
