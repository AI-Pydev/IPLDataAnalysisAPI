from rest_framework import serializers


class IPLSerializer(serializers.Serializer):
    season = serializers.CharField(max_length=4)
