from rest_framework import serializers, mixins
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from notifyapp.models import Log, clean_database


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"


class LogViewSet(ReadOnlyModelViewSet):
    serializer_class = LogSerializer
    queryset = Log.objects.order_by("-created_at")


class FlushSerializer(serializers.Serializer):
    def create(self, validated_data: dict) -> dict:
        clean_database()
        return {}


class FlushViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = FlushSerializer
