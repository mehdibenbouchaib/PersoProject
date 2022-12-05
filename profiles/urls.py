from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProfileDetailViewSet

router = DefaultRouter()
router.register('profile', ProfileDetailViewSet, basename="profile")

urlpatterns = [
    path('', include(router.urls)),
]
