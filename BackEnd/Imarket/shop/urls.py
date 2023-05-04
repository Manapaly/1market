from rest_framework import routers
from django.urls import path
from .views import ShopViewSet, WarehouseViewSet

urlpatterns = [
    path('warehouse_items/<int:min>/<int:max>/',
         WarehouseViewSet.as_view({'get': 'get_warehouse_items_min_max_price'}),
         name='items in range min to max price'),
    path('shops/<int:shop_id>/warehouse_items/',
         WarehouseViewSet.as_view({'get': 'get_warehouse_items_of_shop'}),
         name='get warehouse items from shop'),
    path('shops/<int:shop_id>/put_rating/<int:new_rating>/',
         ShopViewSet.as_view({'get': 'put_rating_to_shop'}), name='rate shop')
]

r = routers.DefaultRouter()

r.register(r'warehouse_items', WarehouseViewSet, basename='warehouse_item')
r.register(r'shops', ShopViewSet, basename='shop')

urlpatterns += r.urls
