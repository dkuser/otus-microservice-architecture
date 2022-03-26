from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from sagaapp.views import OrderViewSet, FlushViewSet, UserViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="Orders",
        default_version="v1",
        description="Order",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


router = routers.DefaultRouter()
router.register(r"orders", OrderViewSet)
router.register(r"flush", FlushViewSet, basename="flush")
router.register(r"users", UserViewSet)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("admin/", admin.site.urls),
    path("", include("django_prometheus.urls")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    *router.urls,
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
