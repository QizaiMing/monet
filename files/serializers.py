from rest_framework import serializers
from .models import ControlFile, DetailFile


class DetailFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailFile
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):

    detail_files = DetailFileSerializer(many=True, read_only=True)

    class Meta:
        model = ControlFile
        fields = [
            "id",
            "NIT",
            "name",
            "partnership_code",
            "tranmission_date",
            "shipping_code",
            "expiry_date",
            "registry_count",
            "transactions_total",
            "details",
            "detail_files",
        ]
