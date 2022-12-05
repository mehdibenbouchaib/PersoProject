from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Profiles


class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error': "you don't have the access "})

        return super(ProfileDetailSerializer, self).validate(data)

    def create(self, validated_data):
        return super(ProfileDetailSerializer, self).create(validated_data)

