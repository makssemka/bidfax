from django.urls import path

from bidfax.auction.api.views import BrandView, BrandDetailView, ModelView, ModelDetailView, LotView, LotDetailView


urlpatterns = [
    path(route='brands/<int:pk>/', view=BrandDetailView.as_view(), name='brands-detail'),
    path(route='brands/', view=BrandView.as_view(), name='brands'),
    path(route='brands/models', view=ModelView.as_view(), name='models'),
    path(route='brands/models/<int:pk>/', view=ModelDetailView.as_view(), name='models'),
    path(route='lots', view=LotView.as_view(), name='lot'),
    path(route='lots/<int:pk>/', view=LotDetailView.as_view(), name='lots-detail')
]
