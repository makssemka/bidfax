from django.urls import path

from bidfax.auction.api.views import BrandView, BrandDetailView, ModelView, ModelDetailView, LotView


urlpatterns = [
    path(route='brands/<int:pk>/', view=BrandDetailView.as_view(), name='brands-detail'),
    path(route='brands/', view=BrandView.as_view(), name='brands'),
    path(route='brands/models', view=ModelView.as_view(), name='models'),
    path(route='brands/models/<int:pk>/', view=ModelDetailView.as_view(), name='models'),
    path(route='lot', view=LotView.as_view(), name='lot')
]
