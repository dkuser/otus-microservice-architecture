from django.contrib.auth import login, authenticate, logout
from rest_framework import viewsets, serializers, mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from api.models import User
from api.permissions import UserPermission


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username"]
        extra_kwargs = {'username': {'read_only': True}}


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [UserPermission]


class UserRegistrationViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    def create(self, validated_data):
        user = authenticate(**validated_data)

        if not user:
            raise serializers.ValidationError('Incorrect username or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return user

    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {'password': {'write_only': True}}


class SessionViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = LoginSerializer
    queryset = User.objects

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)

    def delete(self, request, *_, **__):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
