from rest_framework import mixins, serializers
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from transactionapp.models import Transaction, Balance, clean_database


class TransactionBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("sum", "order_id")


class TransactionBookViewSet(mixins.CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = TransactionBookSerializer
    queryset = Transaction.objects.all()


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = "__all__"


class BalanceViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = BalanceSerializer
    queryset = Balance.objects.all()

    def list(self, request, *args, **kwargs) -> Response:
        balance = Balance.get_solo()

        serializer = self.get_serializer(balance)
        return Response(serializer.data)

    def single_update(self, request, *args, **kwargs) -> Response:
        balance = Balance.get_solo()

        serializer = self.get_serializer(balance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class FlushSerializer(serializers.Serializer):
    def create(self, validated_data: dict) -> dict:
        clean_database()
        return {}


class FlushViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = FlushSerializer


class RollbackOrderViewSet(mixins.DestroyModelMixin, GenericViewSet):
    queryset = Transaction.objects.all()
    lookup_field = "order_id"
    serializer_class = TransactionBookSerializer

    def perform_destroy(self, instance: Transaction) -> None:
        instance.rollback()
