from rest_framework import viewsets, status
from rest_framework.response import Response

from users.permissions import IsAdminOrReadOnly
from .models import Category, Product, ProductImage, SubCategory
from .serializers import ProductSerializer, CategorySerializer, ProductImageSerializer, SubCategorySerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = (IsAdminOrReadOnly,)

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

    def get_subcategory_of_category(self, req, category_id, subcat_id):
        subcategegories = SubCategory.objects.all().filter(category_id=category_id)

        queryset = subcategegories.filter(pk=subcat_id)
        serializer = SubCategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)

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

    def get_subcategory_products(self, req, category_id, subcat_id):
        queryset = Product.objects.all().filter(subcategory_id=subcat_id)
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def put_rating_to_product(self, request, product_id, new_rating) -> Response:
        product = Product.objects.get(id=product_id)
        product.rate_cnt = product.rate_cnt + 1
        product.rating = (product.rating + new_rating) / product.rate_cnt
        product.save()
        return Response(data=product.rating, status=status.HTTP_200_OK)
