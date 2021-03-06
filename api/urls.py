from django.urls import path, include
from rest_framework import routers
from wowmode.api.views import VideolistViewSet
from enticemode.api.views import SequenceViewSet
from mainmenu.api.views import ContentGroupViewSet
from kidszone.api.views import VideoViewSet, ThemeViewSet
from presentationmode.api.views import PresentationViewSet
from globalsettings.api.views import ContentStylingViewSet, VideoWallViewSet

from api import views

router = routers.DefaultRouter()
router.register('wowmode', VideolistViewSet)
router.register('enticemode', SequenceViewSet)
router.register('mainmenu', ContentGroupViewSet)
router.register('kidszonetheme', ThemeViewSet)
router.register('kidszonevideo', VideoViewSet)
router.register('presentation', PresentationViewSet)
router.register('contentstyling', ContentStylingViewSet)
router.register('videowall', VideoWallViewSet)

urlpatterns = [
    path('all/', views.AllAPIView.as_view()),
    path('allmedia/', views.AllMediaView.as_view()),
    path('publish/', views.PublishAPIView.as_view()),
    path('', include(router.urls)),
]
