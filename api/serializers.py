from rest_framework import serializers

from main.models import IpInfo


class IpSerializers(serializers.ModelSerializer):
    class Meta:
        model = IpInfo
        fields = ['id', 'ip', 'city', 'country', 'location', 'postal']


class GetIpSerializers(serializers.ModelSerializer):
    class Meta:
        model = IpInfo
        fields = ['id', 'city', 'country', 'location', 'postal']


class PostIpSerializers(serializers.ModelSerializer):
    class Meta:
        model = IpInfo
        fields = ['ip']
