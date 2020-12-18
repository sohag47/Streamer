from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
# import models
from dashboard.models import ChannelInfo, VideoInfo
# import forms
from dashboard.forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
import time


def home(request):
    channel_name = ChannelInfo.objects.all()
    video_item = VideoInfo.objects.all()
    context = {
        'channel_name': channel_name,
        'video_item': video_item
    }
    return render(request, 'frontend/home.html', context)


def subscribe_view(request, pk):
    post = get_object_or_404(ChannelInfo, pk=pk)
    subscribed = False
    if post.subscribe.filter(pk=request.user.pk).exists():
        post.subscribe.remove(request.user)
        subscribed = False
    else:
        post.subscribe.add(request.user)
        subscribed = True
    return HttpResponseRedirect(reverse('channel_detail', args=[str(pk)]))


@login_required
def channel_detail(request, pk):
    channel_detail_item = get_object_or_404(ChannelInfo, pk=pk)
    channel_name = ChannelInfo.objects.filter(user_name=request.user)
    video_item = VideoInfo.objects.filter(channel_info=pk)

    staff2 = get_object_or_404(ChannelInfo, pk=pk)
    subscribed = False
    if staff2.subscribe.filter(pk=request.user.pk).exists():
        subscribed = True

    context = {
        'channel_detail_item': channel_detail_item,
        'channel_name': channel_name,
        'subscribed': subscribed,
        'video_item': video_item
    }
    return render(request, 'frontend/channel_detail.html', context)


'''
def channel_detail_video(request, pk):
    channel_detail_item = get_object_or_404(ChannelInfo, pk=pk)
    channel_name = ChannelInfo.objects.filter(user_name=request.user)
    video_item = VideoInfo.objects.filter(user_name=request.user)
    context = {
        'channel_detail_item': channel_detail_item,
        'channel_name': channel_name,
        'video_item': video_item
    }
    return render(request, 'frontend/channel_detail_video.html', context)
'''
@login_required
def channel_detail_about(request, pk):
    channel_detail_item = get_object_or_404(ChannelInfo, pk=pk)
    channel_name = ChannelInfo.objects.filter(user_name=request.user)
    staff2 = get_object_or_404(ChannelInfo, pk=pk)
    subscribed = False
    if staff2.subscribe.filter(pk=request.user.pk).exists():
        subscribed = True
    context = {
        'channel_detail_item': channel_detail_item,
        'channel_name': channel_name,
        'subscribed': subscribed,
    }
    return render(request, 'frontend/channel_detail_about.html', context)


@login_required
def video_detail(request, pk):
    video_item_details = get_object_or_404(VideoInfo, pk=pk)
    channel_name = ChannelInfo.objects.filter(user_name=request.user)
    post = video_item_details
    total_subscribe = channel_name.count()
    # view count
    #staff2 = get_object_or_404(ChannelInfo, pk=pk)
    #subscribed = False
    # if staff2.subscribe.filter(pk=request.user.pk).exists():
    #subscribed = True

    #sleeping_time = 3600
    # count seconds
    video_item_details.view = video_item_details.view + 1
    video_item_details.save()
    # if (time.sleep(sleeping_time)):

    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    staff = get_object_or_404(VideoInfo,  pk=pk)
    total_likes = staff.total_likes()
    liked = False
    if staff.like.filter(pk=request.user.pk).exists():
        liked = True

    context = {
        # 'channel_detail_item': channel_detail_item,
        'channel_name': channel_name,
        'video_item_details': video_item_details,
        'total_likes': total_likes,
        'liked': liked,
        'post': post,
        # 'subscribed': subscribed,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'total_subscribe': total_subscribe
    }
    return render(request, 'frontend/video_detail.html', context)


@login_required
def like_view(request, pk):
    post = get_object_or_404(VideoInfo, pk=pk)
    liked = False
    if post.like.filter(pk=request.user.pk).exists():
        post.like.remove(request.user)
        liked = False
    else:
        post.like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('video_detail', args=[str(pk)]))
