import os
from datetime import datetime

from django.contrib.auth import authenticate, login
from django.http import StreamingHttpResponse
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
    queryset = Firm.objects.filter(is_del=False).order_by('-id')
    serializer_class = FirmSerializer
    lookup_field = 'name'

    def perform_destroy(self, instance):
        instance.is_del = True
        instance.save()


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


class DownloadView(APIView):
    def get(self, request):
        def file_iterator(file_name, chunk_size=512):
            with open(file_name, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break

        # 指定需要下载的文件
        download_file = '/Users/bingo/Desktop/practiceProject/test1/manage1.py'
        if not os.path.exists(download_file):
            return Response({"msg": "文件不存在"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        # 将服务器上的文件，通过文件流传输到浏览器
        response = StreamingHttpResponse(file_iterator(download_file))
        # 让文件流写入硬盘，需要对下面两个字段赋值
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format('manage.py')

        return response
