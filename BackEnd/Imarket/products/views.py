from rest_framework import viewsets, status
from rest_framework.response import Response

from users.permissions import IsAdminOrReadOnly
from shop.models import Shop, WarehouseItem
from .models import Category, Product, ProductImage, SubCategory
from .serializers import ProductSerializer, CategorySerializer, ProductImageSerializer, SubCategorySerializer

from django.contrib.postgres.search import SearchVector, TrigramSimilarity, TrigramDistance


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def product_images_of_product(self, request, product_id):
        queryset = ProductImage.objects.all().filter(product_id=product_id)
        serializer = ProductImageSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_subcategories_of_category(self, req, category_id):
        queryset = SubCategory.objects.all().filter(category_id=category_id)
        serializer = SubCategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_min_price_product(self, request, product_id):
        warehouse_items = WarehouseItem.objects.filter(product_id=product_id)
        min_prod = 1e9
        for whi in warehouse_items:
            min_prod = min(min_prod, whi.price)
        return Response({"min_price": min_prod})


    def get_max_price_product(self, request, product_id):
        warehouse_items = WarehouseItem.objects.filter(product_id=product_id)
        max_prod = -1e9
        for whi in warehouse_items:
            max_prod = max(max_prod, whi.price)
        return Response({"min_price": max_prod})

    def get_category_products_rating_price(self,
                                           request,
                                           category_id,
                                           min_rating: int = 0,
                                           min_price: int = 0,
                                           max_price: int = 1e9):
        subcategories = SubCategory.objects.filter(category_id=category_id)
        products = Product.objects.filter(subcategory__in=subcategories).filter(rating__gte=min_rating)
        warehouse_items = WarehouseItem.objects.filter(product__in=products).filter(price__range=(min_price, max_price))
        products = [whi.product for whi in warehouse_items]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def get_subcategory_products_rating_price(self,
                                              request,
                                              subcategory_id,
                                              min_rating: int = 0,
                                              min_price: int = 0,
                                              max_price: int = 1e9):
        products = Product.objects.filter(subcategory_id=subcategory_id).filter(rating__gte=min_rating)
        warehouse_items = WarehouseItem.objects.filter(product__in=products).filter(price__range=(min_price, max_price))
        products = [whi.product for whi in warehouse_items]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def get_subcategory_products(self, request, subcategory_id):
        print("----\n\nJEEE")
        products = Product.objects.filter(subcategory_id=subcategory_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)



    def get_category_products(self, request, category_id):
        subcategories = SubCategory.objects.all().filter(category_id=category_id)
        queryset = Product.objects.filter(subcategory__in=subcategories)

        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def get_products_min_rating(self, request, min):
        queryset = Product.objects.all().filter(rating__gte=min)
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def get_popular_products(self, request):
        queryset = Product.objects.all().order_by('-rating')
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def search_by_name(self, request):
        pattern = request.data['name']
        queryset = Product.objects.filter(name__icontains=pattern)
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def searching(self, request, query):
        results_by_name = Product.objects.filter(name__icontains=query)
        results_by_descr = Product.objects.filter(description__icontains=query)
        results_by_subcat = Product.objects.filter(subcategory__name__icontains=query)
        results_by_cat = Product.objects.filter(subcategory__category__name__icontains=query)
        results = results_by_name.union(results_by_descr).union(results_by_subcat).union(results_by_cat)

        serializer = ProductSerializer(results, many=True)
        return Response(serializer.data)

    def searching_trigram(self, request, query):
        pass

    def put_rating_to_product(self, request, product_id, new_rating) -> Response:
        product = Product.objects.get(id=product_id)
        product.rate_cnt = product.rate_cnt + 1
        product.rating = (product.rating + new_rating) / product.rate_cnt
        product.save()
        return Response(data=product.rating, status=status.HTTP_200_OK)

