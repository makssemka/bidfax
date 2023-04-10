from django.urls import path

from rest_framework import routers

from bidfax.authentication.api.viewsets import UserViewSet
from bidfax.authentication.api.views import ProfileView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path(route='profile/<int:pk>', view=ProfileView.as_view(), name='profiles'),
]

urlpatterns += router.urls
