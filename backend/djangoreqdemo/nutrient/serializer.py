from rest_framework import serializers

import nutrient.models


class NutrientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = nutrient.models.Nutrient
        fields = ['title', 'proteins', "fats", 'carbohydrates']


class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = nutrient.models.Nutrient
        fields = ['id', 'title', 'proteins', "fats", 'carbohydrates']