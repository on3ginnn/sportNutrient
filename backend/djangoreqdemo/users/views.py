from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
import rest_framework.generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import get_user_model

import users.serializer


class UserRegisterAPIView(rest_framework.generics.CreateAPIView):
    serializer_class = users.serializer.RegisterSerializer
    queryset = get_user_model().objects.all()


class UserLoginAPIView(jwt_views.TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        print(response.__dict__)

        return Response({"tokens": response.data}, status=response.status_code)


class UserProfileAPIView(rest_framework.generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = users.serializer.UserSerializer

    def retrieve(self, request, *args, **kwargs):
        self.kwargs = {"pk": request.user.id}

        return super().retrieve(request, *args, **kwargs)


class UserListAPIView(rest_framework.generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = users.serializer.UserSerializer


class UserDetailUpdateDeleteAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = users.serializer.RegisterSerializer
    


class UserSearchAPIView(rest_framework.generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = users.serializer.UserSerializer
    lookup_field = "username"
    
    def retrieve(self, request, *args, **kwargs):
        self.kwargs = {"username":request.GET.get("username")}

        return super().retrieve(request, *args, **kwargs)
