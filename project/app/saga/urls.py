from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView

from sagaapp.views import OrderViewSet, FlushViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r"orders", OrderViewSet)
router.register(r"flush", FlushViewSet, basename="flush")
router.register(r"users", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("django_prometheus.urls")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    *router.urls,
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
