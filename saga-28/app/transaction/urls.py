from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from transactionapp import views

router = routers.DefaultRouter()
router.routes[0].mapping.update({"put": "single_update"})

router.register(r"books", views.TransactionBookViewSet, basename="transactions")
router.register(r"balance", views.BalanceViewSet, basename="balance")
router.register(r"flush", views.FlushViewSet, basename="flush")
router.register(r"orders", views.RollbackOrderViewSet, basename="order")

urlpatterns = [
    path("admin/", admin.site.urls),
    *router.urls,
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
