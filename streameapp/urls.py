from django.urls import path
from . import views
from streameapp.views import home, channel_detail, channel_detail_about, video_detail, like_view, subscribe_view

urlpatterns = [
    path('', views.home, name='home'),
    path('like_post/<int:pk>/', views.like_view, name='like_post'),
    path('subscribe_view/<int:pk>/', views.subscribe_view, name='subscribe_view'),
    path('channel_detail/<pk>/', views.channel_detail, name='channel_detail'),
    path('channel_detail_about/<pk>/',
         views.channel_detail_about, name='channel_detail_about'),

    # path('channel_detail_video/<pk>/',
    # views.channel_detail_video, name='channel_detail_video'),

    path('video_detail/<pk>/', views.video_detail, name='video_detail'),
]
