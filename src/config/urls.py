from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from config.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('bidfax.authentication.urls', 'auth'), namespace='auth')),
    path('api/', include(('bidfax.auction.urls', 'auction'), namespace='auction')),
    # path(route='test/', view=BrandListView.as_view(), name='brands'),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
