from .views import ProductImageViewSet, CategoryViewSet, ProductViewSet, SubCategoryViewSet
from django.urls import path

from rest_framework import routers

urlpatterns = [
    path('categories/<int:category_id>/products/',
         ProductViewSet.as_view({'get': 'get_category_products'}), name='list of category products'),
    path('categories/<int:category_id>/subcategories/',
         SubCategoryViewSet.as_view({'get': 'get_subcategories_of_category'})),
    path('categories/<int:category_id>/subcategories/<int:subcat_id>/',
         SubCategoryViewSet.as_view({'get': 'get_subcategory_of_category'}), name='single subcategory'),
    path('categories/<int:category_id>/subcategories/<int:subcat_id>/products/',
         ProductViewSet.as_view({'get': 'get_subcategory_products'})),
    path('products/rating/<int:min>/',
         ProductViewSet.as_view({'get': 'get_products_min_rating'}), name='products with minimum rate'),
    path('products/<int:product_id>/put_rating/<int:new_rating>/',
         ProductViewSet.as_view({'get': 'put_rating_to_product'}), name='rate product'),

    path('products/<int:product_id>/product_images/',
         ProductImageViewSet.as_view({'get': 'product_images_of_product'}), name='product images of product'),
    path('popular_products/',
         ProductViewSet.as_view({'get': 'get_popular_products'}), name='sorted in desc by rating'),
    path('products/name/',
         ProductViewSet.as_view({'post': 'search_by_name'}), name='search product by name')
]

r = routers.DefaultRouter()

r.register(r'products', ProductViewSet)
r.register(r'product_images', ProductImageViewSet)
r.register(r'categories', CategoryViewSet)

urlpatterns += r.urls
