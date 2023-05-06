from django.core.exceptions import ValidationError
from django.db import models


def validate_rating(value):
    if 0 <= value <= 5:
        return value
    else:
        raise ValidationError("This field accepts rating between 0 and 5")


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', unique=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True, verbose_name='Category Image')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', unique=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return f'subcat {self.pk}: {self.name} -> from cat: {self.category.name}'

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', unique=True)
    main_image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True, verbose_name='Product Main Image')
    is_active = models.BooleanField(default=True, verbose_name='Is Active ?')
    description = models.TextField(null=True, verbose_name='Description')
    rating = models.FloatField(null=True, validators=[validate_rating], default=5.0)
    rate_cnt = models.IntegerField(null=True, default=1)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        # ordering = ('-created_at', )

    def __str__(self):
        return f"id: {self.pk}, {self.name} ({self.subcategory.name})"


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True, verbose_name='Image')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product_images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Image: {self.product.name}'
