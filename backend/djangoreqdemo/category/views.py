from django.contrib.auth import authenticate
from users.serializer import UserSerializer
from rest_framework.views import APIView
import rest_framework.generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import get_user_model

import category.models
import category.serializer


class CategoryCreateAPIView(rest_framework.generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = category.models.Category.objects.all()
    serializer_class = category.serializer.CategoryCreateSerializer


class CategoryListAPIView(rest_framework.generics.ListAPIView):
    queryset = category.models.Category.objects.all()
    serializer_class = category.serializer.CategorySerializer


class CategoryDetailUpdateDeleteAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = category.models.Category.objects.all()
    serializer_class = category.serializer.CategorySerializer
    

class CategorySearchView(APIView):
    """
    Поиск пользователя по username, переданному в заголовке 'username'.
    """
    def get(self, request):
        username = request.query_params.get('username')

        if not username:
            return Response({"ошибка": "юзернейм не передан."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(username=username).first()

        if not user:
            return Response({"ошибка": "юзер не найдет"}, status=status.HTTP_404_NOT_FOUND)

        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
        return Response(user_data, status=status.HTTP_200_OK)