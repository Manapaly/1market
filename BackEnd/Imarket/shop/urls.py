from rest_framework import routers
from django.urls import path
from .views import ShopViewSet, WarehouseViewSet

urlpatterns = [
    path('warehouse_items/<int:min>/<int:max>/products/',
        WarehouseViewSet.as_view({'get': 'get_warehouse_items_min_max_price'}),
        name='items in range min to max price'),
    path('shops/<int:shop_id>/products/',
         WarehouseViewSet.as_view({'get': 'get_shop_warehouse_items'}),
         name='get warehouse items from shop'),
    path('warehouse_items/products/<int:product_id>',
         WarehouseViewSet.as_view({'get': 'get_warehouse_items_of_product'}),
         name='get warehouse items seller, price, quantity'),
]

r = routers.DefaultRouter()

r.register(r'warehouse_items', WarehouseViewSet, basename='warehouse_item')
r.register(r'shops', ShopViewSet, basename='shop')

urlpatterns += r.urls
