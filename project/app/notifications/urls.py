from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from notifyapp import views

router = routers.DefaultRouter()
router.register(r"logs", views.LogViewSet, basename="products")


urlpatterns = [
    path("admin/", admin.site.urls),
    *router.urls,
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
