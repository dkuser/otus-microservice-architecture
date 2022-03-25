from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from deliveryapp import views

router = routers.DefaultRouter()

router.register(r"books", views.DeliveryBookViewSet, basename="deliveries")
router.register(r"couriers", views.CourierViewSet, basename="couriers")
router.register(r"flush", views.FlushViewSet, basename="flush")
router.register(r"orders", views.RollbackOrderViewSet, basename="order")

urlpatterns = [
    path("delivery/admin/", admin.site.urls),
    path("delivery/", include(router.urls)),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
