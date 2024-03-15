from rest_framework import serializers
from rnc.models import DrRnc


class RncSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrRnc
        fields = "__all__"
