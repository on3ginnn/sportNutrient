from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model


class RegisterView(APIView):
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
        
        # Создание JWT-токенов
        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        
        return Response({"message": "User registered successfully", "tokens": tokens}, status=status.HTTP_201_CREATED)


class LoginView(jwt_views.TokenObtainPairView):
    
    def post(self, request, *args, **kwargs):
        # посмотреть как все работает внутри, мозможно это Token.for_user() -> тогда для верификации verify()
        response = super().post(request, *args, **kwargs)
        print(response.__dict__)

        return Response({"tokens": response.data}, status=response.status_code)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        print(request.headers)
        print(request.user)
        print(request.auth)
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_200_OK)
    

# class UserListView(APIView):
class UserListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    """
    Получение списка всех пользователей.
    """
    # def get(self, request):
    #     users = User.objects.all()
    #     users_data = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    #     return Response(users_data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    """
    Получение, обновление и удаление пользователя по ID.
    """
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user_data = {"id": user.id, "username": user.username, "email": user.email}
        return Response([user_data], status=status.HTTP_200_OK)

    def patch(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.password = make_password(password)  # Хэшируем новый пароль

        user.save()
        updated_data = {"id": user.id, "username": user.username, "email": user.email}
        return Response(updated_data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({"message": "юзер удален успешно"}, status=status.HTTP_204_NO_CONTENT)
    

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