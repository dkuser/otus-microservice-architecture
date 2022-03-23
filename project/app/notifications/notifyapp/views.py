from rest_framework import serializers, filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from notifyapp.models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"


class LogViewSet(ReadOnlyModelViewSet):
    serializer_class = LogSerializer
    queryset = Log.objects.order_by("-created_at")
