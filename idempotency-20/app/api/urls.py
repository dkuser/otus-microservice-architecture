from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView

from api.views import UserViewSet, UserRegistrationViewSet, TransactionViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"registration", UserRegistrationViewSet, basename="registration")
router.register(r"transactions", TransactionViewSet)
router.register(r"orders", OrderViewSet)

urlpatterns = [
    path("sessions/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("admin/", admin.site.urls),
    *router.urls,
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
