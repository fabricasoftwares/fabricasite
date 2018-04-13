"""URLs dos endpoints."""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from config import views

router = DefaultRouter()
router.register(r'factory', views.FactoryView, base_name='factory')

urlpatterns = router.urls
