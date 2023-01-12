from django.urls import re_path as url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^cart/', include(('cart.urls',"cart"), namespace='cart')),
    url(r'^orders/', include(('orders.urls','orders'), namespace='orders')),
    url(r'^', include(('shop.urls','shop'), namespace='shop')),
    url(r'^api/', include(('shop.api.urls','api'), namespace='api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)