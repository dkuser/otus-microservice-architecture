from rest_framework import mixins, serializers
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from sagaapp.models import Order
from sagaapp.services import clean_data, OrderService


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("product_id", "quantity", "delivery_date", "id", "result")
        read_only_fields = ["result"]

    def create(self, validated_data: dict) -> Order:
        order = Order(**validated_data)
        OrderService(order).book()
        return order


class OrderViewSet(
    mixins.CreateModelMixin, mixins.DestroyModelMixin, ReadOnlyModelViewSet
):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_destroy(self, instance: Order) -> None:
        OrderService(instance).rollback()


class FlushSerializer(serializers.Serializer):
    def create(self, validated_data: dict) -> dict:
        clean_data()
        return {}


class FlushViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = FlushSerializer
    queryset = Order.objects.all()
