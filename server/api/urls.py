from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'trails', views.TrailViewSet)

urlpatterns = [ url(r'^', include(router.urls)) ]
