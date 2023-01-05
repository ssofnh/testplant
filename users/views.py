from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from .utils import APIResponse
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .serializers import *
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from rest_framework.viewsets import *



class RegisterView(generics.CreateAPIView):
    '''注册接口权限设置'''
    serializer_class = RegisterSerializer
    # 注意需要指定permission_classes = []为空列表或者允许所有权限[rest_framework.permissions.AllowAny]
    permission_classes = []


class UserViewSet(ModelViewSet):
    '''auth_user表：查询、删除等等功能'''
    serializer_class = UserSerializer
    #指定查询集‘数据来源’
    queryset = User.objects.all()
    filter_fields = ['username', 'email','is_active']  # 指定过滤字段
