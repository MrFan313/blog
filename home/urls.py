#coding = utf-8
'''
    标题  进行users子应用的视图路由
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--
'''
#进行users子应用的视图路由
from django.urls import path
from home.views import IndexView,DetailView
urlpatterns = [
    #path的第一个参数:路由
    #第二个参数: 视图函数名
    #首页的路由
    path('',IndexView.as_view(),name = 'index'),
    #详情视图的路由
    path('detail/',DetailView.as_view(),name = 'detail')

]