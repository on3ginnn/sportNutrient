from rest_framework.views import APIView
import rest_framework.generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import nutrient.models
import nutrient.serializer


class NutrientCreateAPIView(rest_framework.generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = nutrient.models.Nutrient.objects.all()
    serializer_class = nutrient.serializer.NutrientCreateSerializer
"""
{
    "title": "кола",
    "proteins": "10",
    "fats": "50",
    "carbohydrates": "80"
}
"""

class NutrientListAPIView(rest_framework.generics.ListAPIView):
    queryset = nutrient.models.Nutrient.objects.all()
    serializer_class = nutrient.serializer.NutrientSerializer


class NutrientDetailUpdateDeleteAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = nutrient.models.Nutrient.objects.all()
    serializer_class = nutrient.serializer.NutrientSerializer
{
    "title": "Кока Кола"
}