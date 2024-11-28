from rest_framework import serializers

import product.models


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = product.models.Item
        fields = ['title', 'description', "category"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product.models.Item
        fields = ['id', 'title', 'description', "category"]