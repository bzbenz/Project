from django.utils import timezone
from rest_framework import serializers

from apps.accounts.serializers import AccountSerializer
from apps.categories.models import Category
from apps.category_product.models import CategoryProduct
from apps.products.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(required=False, queryset=Product.objects.all())
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['product', 'image']

    def get_image(self, obj):
        return "http://172.20.10.9:8000/" + obj.image.url


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True, read_only=True)
    property = serializers.SerializerMethodField()
    first_image_url = serializers.SerializerMethodField()
    freight_detail = serializers.SerializerMethodField()
    seller_data = serializers.SerializerMethodField()
    sub_total = serializers.SerializerMethodField()
    quality = serializers.SerializerMethodField()
    price = serializers.IntegerField()
    freight_fee = serializers.IntegerField()
    x = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = []

    @staticmethod
    def get_property(obj):
        return obj.properties

    @staticmethod
    def get_first_image_url(obj):
        first_image = obj.images.first()
        if first_image is None:
            return ""
        else:
            return "http://172.20.10.9:8000/" + first_image.image.url

    @staticmethod
    def get_freight_detail(obj):
        return obj.get_freight_display()

    @staticmethod
    def get_quality(obj):
        return obj.get_product_quality_display()

    @staticmethod
    def get_category(obj):
        categories = CategoryProduct.objects.filter(product_id=obj.id, category__category_type=Category.normal)
        if categories.count() > 0:
            return categories[0].category.name
        else:
            return ""

    @staticmethod
    def get_seller_data(obj):
        return AccountSerializer(obj.seller).data

    @staticmethod
    def get_sub_total(obj):
        return obj.price + obj.freight_fee

    @staticmethod
    def get_x(obj):
        delta_time = obj.exp_date_promotion - timezone.now()
        x = round(delta_time.total_seconds())
        return x


class SimpleProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = []