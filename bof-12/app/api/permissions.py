from django.db.models import Model
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from api.models import User


class UserPermission(IsAuthenticated):
    def has_object_permission(self, request: Request, view: APIView, obj: Model) -> bool:
        user = request.user
        if isinstance(obj, User):
            return obj.id == user.id
        return super().has_object_permission(request, view, obj)
