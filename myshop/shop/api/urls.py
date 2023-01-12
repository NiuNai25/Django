from django.urls import re_path as url, include,path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('category', views.CategoryViewSet)
router.register('orderitem', views.OrderItemViewSet)
router.register('order', views.OrderViewSet)



urlpatterns = [
    # ...
    url(r'^', include(router.urls)),
    url(r'^category/(?P<pk>\d+)/add/$', views.CategoryAddView.as_view(), name='category_add'),
    url(r'^category/(?P<pk>\d+)/update/$', views.CategoryUpdateView.as_view(), name='category_update'),
    url(r'^category/(?P<pk>\d+)/delete/$', views.CategoryDelete.as_view(), name='category_del'),
    url(r'^product/(?P<pk>\d+)/update/$', views.ProductUpdateView.as_view(), name='product_update'),
    url(r'^delete/(?P<pk>\d+)/order/$', views.OrderDelete.as_view(), name='order_del'),
]