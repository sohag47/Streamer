from streameapp.views import video_detail
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
# import models
from dashboard.models import ChannelInfo, VideoInfo
from accounts.models import ExtraUserInfo
from accounts.forms import ExtraUserInfoForm
# import Forms
from dashboard.forms import ChannelInfoForm, VideoInfoForm
# Create your views here.

# CURD Operation for Channel
# Read Operation:
@login_required
def dashboard_home(request):
    channel_name = ChannelInfo.objects.filter(user_name=request.user)
    user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    context = {
        'channel_name': channel_name,
        'user_extra': user_extra
    }
    return render(request, 'dashboard/dashboard_home.html', context)


@login_required
# Create Operation:
def dashboard_create_channel(request):
    if request.method == "POST":
        form = ChannelInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ChannelInfoForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/create_channel.html', context)


@login_required
# Update Operation:
def edit_channel(request, pk):
    channel = get_object_or_404(ChannelInfo, pk=pk)
    if request.method == "POST":
        form = ChannelInfoForm(request.POST, request.FILES, instance=channel)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ChannelInfoForm(instance=channel)
    context = {
        'form': form
    }
    return render(request, 'dashboard/edit_channel.html', context)


@login_required
# Delete Operation:
def delete_channel(request, pk):

    obj = get_object_or_404(ChannelInfo, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    context = {
        'obj': obj
    }
    return render(request, "dashboard/delete_channel.html", context)


@login_required
# CURD Operation for Video:
# Read Operation:
def allvideos_list(request):
    context = {}
    video_detail = VideoInfo.objects.filter(user_name=request.user)
    context = {
        'video_detail': video_detail
    }
    return render(request, 'dashboard/allvideos_list.html', context)


@login_required
# Create Operation:
def dashboard_create_video(request):
    if request.method == "POST":
        form = VideoInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = VideoInfoForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/create_video.html', context)


@login_required
# Update Operation:
def edit_video(request, pk):
    video = get_object_or_404(VideoInfo, pk=pk)
    if request.method == "POST":
        form = VideoInfoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = VideoInfoForm(instance=video)
    context = {
        'form': form
    }
    return render(request, 'dashboard/edit_video.html', context)


@login_required
# Delete Operation:
def delete_video(request, pk):
    obj = get_object_or_404(VideoInfo, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('allvideos_list')
    context = {
        'obj': obj
    }
    return render(request, "dashboard/delete_video.html", context)


@login_required
# CURD Operation for extra user info:
# Create User info operation
def create_user_extra_info(request):
    if request.method == "POST":
        form = ExtraUserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExtraUserInfoForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/create_user_extra_info.html', context)


@login_required
# Update Operation:
def edit_user_extra_info(request, pk):
    user_extra_info = get_object_or_404(ExtraUserInfo, pk=pk)
    if request.method == "POST":
        form = ExtraUserInfoForm(
            request.POST, request.FILES, instance=user_extra_info)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExtraUserInfoForm(instance=user_extra_info)
    context = {
        'form': form
    }
    return render(request, 'dashboard/edit_user_extra_info.html', context)


@login_required
# Delete Operation:
def delete_user_extra_info(request, pk):

    obj = get_object_or_404(ExtraUserInfo, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('dashboard')
    context = {
        'obj': obj
    }
    return render(request, "dashboard/delete_user_extra_info.html", context)
