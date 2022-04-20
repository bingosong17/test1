from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FirmSerializer, UserSerialize, AuthTokenSerializer
from .models import Firm
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
from django.contrib import auth
import base64
from django.contrib.auth.models import User


# Create your views here.
class FirmViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Firm.objects.filter(is_active=True)
    serializer_class = FirmSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            # user = User.objects.filter(is_active=True, username=username)
            # if user:
            #     print('lalal')
            user = authenticate(username=username, password=password)
            if user:
                print('llllllll')

            # user.last_login = now()
            # user.save()
            # token = generate_jwt(user)
            # token = base64.b64encode('admin:password123')
            # user_serialize = UserSerialize(user)
            return Response({'token': '123', 'user': "user_serialize.data"}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "用户名或密码错误！"}, status=status.HTTP_400_BAD_REQUEST)
