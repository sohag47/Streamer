"""streamer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# for django images
from django.conf import settings
from . import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("streameapp.urls")),
    path('dashboard/', include("dashboard.urls")),

    # Signup url
    path('signup/', accounts_views.signup, name='signup'),

    # Login url:
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # Logout url:
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # password reset:
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), name='password_reset'
    ),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'
    ),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'
    ),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'
    ),
    # password change:
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html'), name='password_change'
    ),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'), name='password_change_done'
    ),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # for django images

handler404 = 'streameapp.views.error_404_not_found'
