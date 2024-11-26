from django.contrib import admin
from django.urls import path, include
import rest_framework
from rest_framework_simplejwt import views as jwt_views
import users


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('auth/', include('users.urls'))
]
