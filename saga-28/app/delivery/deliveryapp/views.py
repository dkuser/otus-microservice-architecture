from rest_framework import mixins, serializers
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from deliveryapp.models import Delivery, Courier, clean_database


class DeliveryBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ("date", "order_id", "courier")
        read_only_fields = ["courier"]


class DeliveryBookViewSet(mixins.CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = DeliveryBookSerializer
    queryset = Delivery.objects.all()


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = "__all__"
        read_only_fields = ["is_free"]


class CourierViewSet(mixins.CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = CourierSerializer
    queryset = Courier.objects.all()


class FlushSerializer(serializers.Serializer):
    def create(self, validated_data: dict) -> dict:
        clean_database()
        return {}


class FlushViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = FlushSerializer


class RollbackOrderViewSet(mixins.DestroyModelMixin, GenericViewSet):
    queryset = Delivery.objects.all()
    lookup_field = "order_id"
    serializer_class = DeliveryBookSerializer

    def perform_destroy(self, instance: Delivery) -> None:
        instance.rollback()
