from rest_framework import mixins, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from transactionapp.models import Transaction, Balance, clean_database


class TransactionSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="balance.user_id", read_only=True)

    class Meta:
        model = Transaction
        exclude = ("balance",)
        read_only_fields = ("created_at",)

    def create(self, validated_data: dict) -> Transaction:
        user_id = validated_data.pop("user_id")
        transaction = Transaction(**validated_data)
        transaction.save_with_user(user_id)
        return transaction


class TransactionBookSerializer(TransactionSerializer):
    user_id = serializers.IntegerField(source="balance.user_id")

    def create(self, validated_data: dict) -> Transaction:
        balance = validated_data.pop("balance")
        validated_data["user_id"] = balance["user_id"]
        return super().create(validated_data)


class TransactionBookViewSet(mixins.CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = TransactionBookSerializer
    queryset = Transaction.objects.all()


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = "__all__"


class BalanceViewSet(ReadOnlyModelViewSet):
    serializer_class = BalanceSerializer
    queryset = Balance.objects.all()


class FlushSerializer(serializers.Serializer):
    def create(self, validated_data: dict) -> dict:
        clean_database()
        return {}


class FlushViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = FlushSerializer


class RollbackOrderViewSet(mixins.DestroyModelMixin, GenericViewSet):
    queryset = Transaction.objects.all()
    lookup_field = "order_id"
    serializer_class = TransactionSerializer

    def perform_destroy(self, instance: Transaction) -> None:
        instance.rollback()


class TransactionViewSet(mixins.CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(user_id=self.request.user.id)


class UserBalanceViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = BalanceSerializer
    queryset = Balance.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs) -> Response:
        balance, _ = Balance.objects.get_or_create(
            user_id=self.request.user.id, defaults={"sum": 0}
        )

        serializer = self.get_serializer(balance)
        return Response(serializer.data)
