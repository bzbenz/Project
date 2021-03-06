from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import serializers

from apps.orders.models import Order, OrderItem
from apps.products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()


    class Meta:
        model = OrderItem
        exclude = []
        extra_kwargs = {
            'order': {
                'required': False
            }
        }


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        exclude = []

    def create(self, validated_data):
        try:
            with transaction.atomic():
                order_items = validated_data.pop('order_items')

                order = super(OrderSerializer, self).create(validated_data)

                for order_item in order_items:
                    OrderItem.objects.create(
                        order=order,
                        **order_item
                    )

        except KeyError:
            raise ValidationError('send the data properly')
        else:
            return order
