"""URL dos enpoints."""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from section import views

router = DefaultRouter()
router.register(r'sections', views.SectionView, base_name='sections')

urlpatterns = router.urls
