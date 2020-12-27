from django.urls import path
from . import views
from streameapp.views import home, channel_detail, channel_detail_about, video_detail, like_view, history_view, subscribe_view, search_result_view, subscription_view, delete_comments, update_comments

urlpatterns = [
    path('', views.home, name='home'),
    path('subscription_view/', views.subscription_view, name='subscription_view'),
    path('search/', views.search_result_view, name='search'),
    path('like_post/<int:pk>/', views.like_view, name='like_post'),
    path('subscribe_view/<int:pk>/', views.subscribe_view, name='subscribe_view'),
    path('channel_detail/<pk>/', views.channel_detail, name='channel_detail'),
    path('channel_detail_about/<pk>/',
         views.channel_detail_about, name='channel_detail_about'),
    #path('create_comment/', views.create_comment, name='create_comment'),
    path('update_comments/<pk>/', views.update_comments, name='update_comments'),
    path('delete_comments/<pk>/', views.delete_comments, name='delete_comments'),

    path('video_detail/<pk>/', views.video_detail, name='video_detail'),
    path('history/', views.history_view, name='history'),

]
