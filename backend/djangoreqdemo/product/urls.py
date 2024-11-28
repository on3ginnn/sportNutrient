import django.urls

import product.views


urlpatterns = [
    django.urls.path('create/', product.views.ProductCreateAPIView.as_view(), name='create'),
    django.urls.path('all/', product.views.ProductListAPIView.as_view(), name='list'),
    django.urls.path('<int:pk>/', product.views.ProductDetailUpdateDeleteAPIView.as_view(), name='concrete'),
    django.urls.path('category/search/', product.views.ProductSearchView.as_view(), name='search'),
]
