from rest_framework import serializers
import category.models


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = category.models.Category
        fields = ['title', "slug"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category.models.Category
        fields = ['id', 'title', "slug"]