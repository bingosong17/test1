from datetime import datetime

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser
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
    queryset = Firm.objects.all().order_by('-id')
    serializer_class = FirmSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                user.last_login = now()
                user.save()
                token = base64.b64encode(f"{username}:{password}".encode())
                user_serialize = UserSerialize(user)
                return Response({'token': token, 'user': user_serialize.data}, status=status.HTTP_200_OK)
            else:
                return Response({"msg": "用户名或密码错误！"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg": "用户名或密码错误！"}, status=status.HTTP_400_BAD_REQUEST)


class UploadView(APIView):
    '''
    上传文件接口
    '''

    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        print(request.data)
        # 获取多个file
        files = request.FILES.getlist('file', None)
        for file_obj in files:
            # 将文件缓存到本地后上传
            local_file = './' + file_obj.name
            # 读取传入的文件
            destination = open(local_file, 'wb+')
            try:
                for chunk in file_obj.chunks():  # 分块写入文件
                    destination.write(chunk)
            finally:
                destination.close()

        return Response({"msg": "上传成功"}, status=status.HTTP_200_OK)
