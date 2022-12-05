from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Profiles
from profiles.serializers import ProfileDetailSerializer


class ProfileDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        profile = Profiles.objects.all()
        return profile
