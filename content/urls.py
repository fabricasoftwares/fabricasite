"""URLs dos endpoints."""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from content import views

router = DefaultRouter()
router.register(r'features', views.FeatureView)
router.register(r'members', views.MembersView, base_name='members')
router.register(r'projects', views.ProjectView)

urlpatterns = router.urls
