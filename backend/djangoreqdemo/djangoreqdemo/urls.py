from django.contrib import admin
from django.urls import path, include
import rest_framework
import users


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('users.urls'))
]
