from django.contrib.auth.backends import ModelBackend
from .models import *
from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, code=200, msg='成功', data=None, status=None,
                 headers=None, content_type=None, **kwargs):
        dic = {'status': code, 'msg': msg}
        if data:
            dic['data'] = data
        dic.update(kwargs)
        super().__init__(data=dic, status=status, headers=headers, content_type=content_type)

# class CustomBackend(ModelBackend):
#     """
#     自定义用户验证，定义完之后还需要在settings中进行配置
#     """
#     def authenticate(self, username=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(username=username)
#             # django里面的password是加密的，前端传过来的password是明文，
#             # 调用check_password就会对明文进行加密，比较两者是否相同
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None



"""
    自定义jwt认证成功返回数据
    :token
    返回的jwt
    :user
    当前登录的用户信息[对象]
    :request
    当前本次客户端提交过来的数据
    :role
    角色
"""

def jwt_response_payload_handler(token, user=None, request=None, role=None):

    if user.first_name:
        name = user.first_name
    else:
        name = user.username
    return {
        "authenticated": 'true',
        "code":"200",
        'data':{
            'id': user.id,
            # "role": role,
            # 'name': name,
            'username': user.username,
            # 'data':user.username,
            'email': user.email,
            'token': token,

        },

    }

