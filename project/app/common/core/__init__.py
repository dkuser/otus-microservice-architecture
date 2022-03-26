import os

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .authentication import JWTAuthenticationVirtualUser


def init_migrations() -> None:
    user = User.objects.create_superuser(
        "admin", "admin@admin.ru", password=os.environ["ROOT_PASSWORD"]
    )
    Token.objects.create(user=user, key=os.environ["ROOT_TOKEN"])
