from rest_framework import serializers

from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}
