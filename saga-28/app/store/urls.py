from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from storeapp import views

router = routers.DefaultRouter()
router.register(r"books", views.StoreBookViewSet, basename="books")
router.register(r"products", views.ProductViewSet, basename="products")
router.register(r"flush", views.FlushViewSet, basename="flush")
router.register(r"orders", views.RollbackOrderViewSet, basename="order")

urlpatterns = [
    path("admin/", admin.site.urls),
    *router.urls,
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
