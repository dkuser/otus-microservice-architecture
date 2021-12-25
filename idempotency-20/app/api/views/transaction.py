from django.db.models import QuerySet
from rest_framework import mixins, serializers
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import Transaction
from api.permissions import UserPermission


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        extra_kwargs = {"created_at": {"read_only": True}, "user": {"read_only": True}}


class TransactionViewSet(mixins.CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = [UserPermission]

    def get_queryset(self) -> QuerySet:
        return self.request.user.transaction_set

    def perform_create(self, serializer: serializers.Serializer) -> None:
        serializer.save(user=self.request.user)

