from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    # The method will get "get_" in front
    def get_my_discount(self, obj):
        print("obj in seralizer => ", obj.id)
        return obj.get_discount()