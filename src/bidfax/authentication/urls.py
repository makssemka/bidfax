from django.urls import path

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from bidfax.authentication.api.viewsets import UserViewSet
from bidfax.authentication.api.views import ProfileView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path(route='profile/<int:pk>', view=ProfileView.as_view(), name='profiles'),
    path(route='token/login', view=obtain_auth_token, name='login')
]

urlpatterns += router.urls
