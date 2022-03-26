from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from finderapp import views

router = routers.DefaultRouter()
router.register(r"products", views.ProductViewSet, basename="products")
router.register(r"flush", views.FlushViewSet, basename="flush")


urlpatterns = [
    path("finder/admin/", admin.site.urls),
    path("finder/", include(router.urls)),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
