from django.urls import path
from . import views
from dashboard.views import create_user_extra_info, edit_user_extra_info, delete_user_extra_info
# all channel url:
from dashboard.views import dashboard_create_channel, edit_channel, delete_channel
# all video url
from dashboard.views import dashboard_home, allvideos_list, dashboard_create_video, edit_video, delete_video
urlpatterns = [
    path('create_user_extra_info/', views.create_user_extra_info,
         name='create_user_extra_info'),
    path('edit_user_extra_info/<int:pk>/', views.edit_user_extra_info,
         name='edit_user_extra_info'),
    path('delete_user_extra_info/<int:pk>/',
         views.delete_user_extra_info, name='delete_user_extra_info'),
    # CURD Channel url:
    path('', views.dashboard_home, name='dashboard'),
    path('create_channel/', views.dashboard_create_channel, name='create_channel'),
    path('edit_channel/<int:pk>/', views.edit_channel, name='edit_channel'),
    path('delete_channel/<int:pk>/', views.delete_channel, name='delete_channel'),
    # CURD Video url:
    path('create_video/', views.dashboard_create_video, name='create_video'),
    path('allvideos_list/', views.allvideos_list, name='allvideos_list'),
    path('edit_video/<int:pk>/', views.edit_video, name='edit_video'),
    path('delete_video/<int:pk>/', views.delete_video, name='delete_video'),
]
