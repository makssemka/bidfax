from django.contrib import admin
from django.urls import path, include

from config.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('bidfax.authentication.urls', 'auth'), namespace='auth')),
]

urlpatterns += doc_urls
