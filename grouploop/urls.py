from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('circles/', views.CircleList.as_view(), name='circle_list'),
    path('circles/<int:pk>', views.CircleDetail.as_view(), name='circle_detail'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail')
]
