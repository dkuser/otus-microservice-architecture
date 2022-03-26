from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from notifyapp import views

router = routers.DefaultRouter()
router.register(r"logs", views.LogViewSet, basename="products")
router.register(r"flush", views.FlushViewSet, basename="flush")


urlpatterns = [
    path("notifications/admin/", admin.site.urls),
    path("notifications/", include(router.urls)),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
