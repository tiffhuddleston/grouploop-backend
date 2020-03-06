from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('circles/', views.CircleList.as_view(), name='circle_list'),
    path('circles/<int:pk>', views.CircleDetail.as_view(), name='circle_detail'),
    path('members/', views.MemberList.as_view(), name='member_list'),
    path('members/<int:pk>', views.MemberDetail.as_view(), name='member_detail')
]
