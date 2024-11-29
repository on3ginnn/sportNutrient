from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import get_user_model

from users.serializer import UserSerializer


class UserRegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        # Проверка обязательных полей
        if not username or not password or not email:
            return Response({"message": "Все поля обязательны для заполнения."}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка уникальности username
        if User.objects.filter(username=username).exists():
            return Response({"message": "Пользователь с таким ником уже существует."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Создание пользователя
        user = User.objects.create_user(username=username, email=email, password=password)
               
        return Response({"message": "Пользователь успешно создан"}, status=status.HTTP_201_CREATED)


class UserLoginAPIView(jwt_views.TokenObtainPairView):
    
    def post(self, request, *args, **kwargs):
        # посмотреть как все работает внутри, мозможно это Token.for_user() -> тогда для верификации verify()
        response = super().post(request, *args, **kwargs)
        print(response.__dict__)

        return Response({"tokens": response.data}, status=response.status_code)


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_200_OK)
    

class UserListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    

class UserSearchView(APIView):
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