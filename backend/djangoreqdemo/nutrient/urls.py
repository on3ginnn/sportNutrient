import django.urls

import nutrient.views


urlpatterns = [
    django.urls.path('create/', nutrient.views.NutrientCreateAPIView.as_view(), name='create'),
    django.urls.path('all/', nutrient.views.NutrientListAPIView.as_view(), name='list'),
    django.urls.path('<int:pk>/', nutrient.views.NutrientDetailUpdateDeleteAPIView.as_view(), name='concrete'),
]
