


from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('login', obtain_jwt_token),   # jwt中提供了一个认证，直接导入后使用obtain_jwt_token视图即可
    path('Register', views.RegisterView.as_view()),


]

#以下只能配合视图集使用
router = DefaultRouter() #创建路由器  SimpleRouter与DefaultRouter只有一个区别，DefaultRouter会生成一个根路由
router.register('user',views.UserViewSet) #注册路由
urlpatterns += router.urls #把生成好的路由拼接到urlpatterns
