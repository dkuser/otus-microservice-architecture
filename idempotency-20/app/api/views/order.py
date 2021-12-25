from django.db.models import QuerySet
from rest_framework import mixins, serializers
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import Order
from api.permissions import UserPermission


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {"user": {"read_only": True}}


class OrderViewSet(mixins.CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [UserPermission]

    def get_queryset(self) -> QuerySet:
        return self.request.user.order_set

    def perform_create(self, serializer: serializers.Serializer) -> None:
        serializer.save(user=self.request.user)
