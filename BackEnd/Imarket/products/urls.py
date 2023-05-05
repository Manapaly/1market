from .views import ProductImageViewSet, CategoryViewSet, ProductViewSet, SubCategoryViewSet
from django.urls import path

from rest_framework import routers

urlpatterns = [
    path('categories/<int:category_id>/products/',
         ProductViewSet.as_view({'get': 'get_category_products'}), name='list of category products'),
    path('categories/<int:category_id>/subcategories/',
         SubCategoryViewSet.as_view({'get': 'get_subcategories_of_category'})),

    path('products/rating/<int:min>/',
         ProductViewSet.as_view({'get': 'get_products_min_rating'}), name='products with minimum rate'),
    path('products/<int:product_id>/put_rating/<int:new_rating>/',
         ProductViewSet.as_view({'get': 'put_rating_to_product'}), name='rate product'),

    path('products/<int:product_id>/product_images/',
         ProductImageViewSet.as_view({'get': 'product_images_of_product'}), name='product images of product'),
    path('popular_products/',
         ProductViewSet.as_view({'get': 'get_popular_products'}), name='sorted in desc by rating'),
    path('products/name/',
         ProductViewSet.as_view({'post': 'search_by_name'}), name='search product by name'),




    # searching
    path('products/searching/<str:query>/',
         ProductViewSet.as_view({'get': 'searching'}), name='search product'),


    path('products/<int:product_id>/min_price/',
         ProductViewSet.as_view({'get': 'get_min_price_product'}), name='get_min_price_product'),
    path('products/<int:product_id>/max_price/',
         ProductViewSet.as_view({'get': 'get_max_price_product'}), name='get_max_price_product'),

    path('products/categories/<int:category_id>/rating/<int:min_rating>/price/<int:min_price>/<int:max_price>/',
         ProductViewSet.as_view({'get': 'get_category_products_rating_price'}),
         name='get category products by rating and price'),
    path('products/subcategories/<int:subcategory_id>/rating/<int:min_rating>/price/<int:min_price>/<int:max_price>/',
         ProductViewSet.as_view({'get': 'get_subcategory_products_rating_price'}),
         name='get subcategory products by rating and price'),

    path('products/subcategories/<int:subcategory_id>/',
         ProductViewSet.as_view({'get': 'get_subcategory_products'}),
         name='get subcategory products '),

]

r = routers.DefaultRouter()

r.register(r'products', ProductViewSet)
r.register(r'product_images', ProductImageViewSet)
r.register(r'categories', CategoryViewSet)

urlpatterns += r.urls
