from rest_framework import serializers

from main.models import IpInfo


class IpSerializers(serializers.ModelSerializer):
    class Meta:
        model = IpInfo
        fields = ['id', 'city', 'country', 'location', 'postal']