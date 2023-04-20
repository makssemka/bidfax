from django.urls import path

from rest_framework import routers

from bidfax.authentication.api.viewsets import UserViewSet
from bidfax.authentication.api.views import ProfileView, TokenView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path(route='profile/<uuid:user__uid>', view=ProfileView.as_view(), name='profiles'),
    path(route='token/login', view=TokenView.as_view(), name='login')
]

urlpatterns += router.urls
