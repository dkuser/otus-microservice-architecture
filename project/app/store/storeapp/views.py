from rest_framework import mixins, serializers
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, GenericViewSet

from storeapp.models import GoodMovement, Product, clean_database


class StoreBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodMovement
        fields = ("product", "quantity", "order_id", "sum")
        read_only_fields = ["sum"]


class StoreBookViewSet(mixins.CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = StoreBookSerializer
    queryset = GoodMovement.objects.all()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductClientViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class FlushSerializer(serializers.Serializer):
    def create(self, validated_data: dict) -> dict:
        clean_database()
        return {}


class FlushViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = FlushSerializer


class RollbackOrderViewSet(mixins.DestroyModelMixin, GenericViewSet):
    queryset = GoodMovement.objects.all()
    lookup_field = "order_id"
    serializer_class = StoreBookSerializer

    def perform_destroy(self, instance: GoodMovement) -> None:
        instance.rollback()
