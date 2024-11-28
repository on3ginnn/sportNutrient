from rest_framework.views import APIView
import rest_framework.generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import product.models
import product.serializer


class ProductCreateAPIView(rest_framework.generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = product.models.Item.objects.item_all()
    serializer_class = product.serializer.ProductCreateSerializer


class ProductListAPIView(rest_framework.generics.ListAPIView):
    queryset = product.models.Item.objects.item_all()
    serializer_class = product.serializer.ProductSerializer


class ProductDetailUpdateDeleteAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = product.models.Item.objects.item_all()
    serializer_class = product.serializer.ProductSerializer
    

class ProductSearchView(APIView):
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