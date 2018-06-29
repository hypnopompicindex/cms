from drf_multiple_model.views import ObjectMultipleModelAPIView, FlatMultipleModelAPIView
from wowmode.api.serializers import *
from wowmode.models import Videolist, Video
from wowmode.models import Video as WowModeVideo
from enticemode.api.serializers import *
from enticemode.models import Sequence
from mainmenu.api.serializers import *
from mainmenu.models import ContentGroup, ContentGallery
from kidszone.api.serializers import *
from kidszone.models import Video, Theme
from presentationmode.api.serializers import *
from presentationmode.models import Presentation
from globalsettings.api.serializers import *
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
        {'queryset': Publish.objects.all(), 'serializer_class': PublishSerializer,
         'label': 'Publish', },
    )


class AllMediaView(FlatMultipleModelAPIView):
    add_model_type = False

    querylist = (
        {'queryset': Video.objects.all().distinct(), 'serializer_class': VideoVideoTimestampSerializer},
        {'queryset': Video.objects.all().distinct(), 'serializer_class': VideoImageTimestampSerializer},
        {'queryset': Theme.objects.all().distinct(), 'serializer_class': ThemeBackgroundImageTimestampSerializer},
        {'queryset': Theme.objects.all().distinct(), 'serializer_class': ThemeBubbleImageTimestampSerializer},
        {'queryset': Sequence.objects.all().distinct(), 'serializer_class': SequenceIntroVideoSerializer},
        {'queryset': Sequence.objects.all().distinct(), 'serializer_class': SequenceOutroVideoSerializer},
        {'queryset': Sequence.objects.all().distinct(), 'serializer_class': SequenceTouchIndicatorVideoSerializer},
        {'queryset': Sequence.objects.all().distinct(), 'serializer_class': SequenceBackgroundVignetteVideoSerializer},
        {'queryset': ContentStyling.objects.all().distinct(), 'serializer_class': ContentStylingImageSerializer},
        {'queryset': Presentation.objects.all(), 'serializer_class': PresentationImageOverlaySerializer},
        {'queryset': WowModeVideo.objects.all(), 'serializer_class': VideoFileSerializer},
        {'queryset': ContentGallery.objects.all(), 'serializer_class': ContentGalleryImageSerializer},
        {'queryset': ContentGroup.objects.all(), 'serializer_class': ContentGroupButtonImageSerializer},
        {'queryset': ContentCard.objects.all(), 'serializer_class': ContentCardVideoSerializer},
        {'queryset': ContentCard.objects.all(), 'serializer_class': ContentCardButtonImageSerializer},
        {'queryset': ContentCard.objects.all(), 'serializer_class': ContentCardGradientOverlaySerializer},
    )
