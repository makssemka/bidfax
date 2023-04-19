from django.urls import path

from rest_framework import routers

from bidfax.authentication.api.viewsets import UserViewSet
from bidfax.authentication.api.views import ProfileView, TokenCreateView, TokenDeleteView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path(route='profile/<int:pk>', view=ProfileView.as_view(), name='profiles'),
    path(route='token/login', view=TokenCreateView.as_view(), name='login'),
    path(route='token/logout', view=TokenDeleteView.as_view(), name='logout')
]

urlpatterns += router.urls
