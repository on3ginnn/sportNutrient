from django.contrib import admin
from django.urls import path, include
import rest_framework
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('auth/', include('users.urls')),
    path('category/', include('category.urls')),
    path('item/', include('product.urls')),

    path('admin/', admin.site.urls),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]
