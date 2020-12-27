from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
# import models
from dashboard.models import ChannelInfo, VideoInfo, Comments, HistoryInfo
# import forms
from dashboard.forms import CommentForm, HistoryInfoForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
# Create your views here.
import time
from django.db.models import Q

# 404 Not Found operation:
# when type wrong url then server show 404 not found page without any error


def error_404_not_found(request, exception):
    return render(request, '404_Not_found.html', {})


def home(request):
    channel_name = ChannelInfo.objects.all()
    video_item = VideoInfo.objects.all()
    context = {
        'channel_name': channel_name,
        'video_item': video_item
    }
    return render(request, 'frontend/home.html', context)


def search_result_view(request):
    #channel_name = ChannelInfo.objects.filter(name=query)
    context = {}

    query = request.GET.get('q')
    # print(query)
    lookups = Q(keyword__icontains=query)
    video_item = VideoInfo.objects.filter(lookups).distinct()

    context = {
        'video_item': video_item,
        'query': query
    }
    return render(request, 'frontend/search_result_view.html', context)


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
    staff2 = get_object_or_404(
        ChannelInfo, pk=video_item_details.channel_info.pk)
    total_subscribe = staff2.total_subscriber
    #subscribed = False
    # if staff2.subscribe.filter(pk=request.user.pk).exists():
    #subscribed = True
    #user = request.user
    #instance = pk

    #video = instance
    #history = HistoryInfo(instance=pk, user_name=user)
    # history.save()
    # view option:
    #sleeping_time = 3600
    # count seconds
    video_item_details.view = video_item_details.view + 1
    video_item_details.save()
    # if (time.sleep(sleeping_time)):

    # like option:
    staff = get_object_or_404(VideoInfo,  pk=pk)
    total_likes = staff.total_likes()
    liked = False
    if staff.like.filter(pk=request.user.pk).exists():
        liked = True
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
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


# Comment Operations:
'''
# create comment:
def create_comment(request):
    # comment form start:
    #new_comment = None
    if request.method == 'POST':
        video_infos = get_object_or_404(VideoInfo, video_id)
        name = request.POST['name']
        comment = request.POST['comment']
        video_id = request.POST['video_id']
        new_comment = Comments(post=video_id, name=name, body=comment)
        new_comment.save()
        print(name)
        print(comment)
        print(video_id)
        return HttpResponseRedirect('/')
        #id = int(14)
        # return HttpResponseRedirect('/channel_detail/%d' % id)
    # else:
        # pass
        #id = int(post.pk)
        # return HttpResponseRedirect('/channel_detail/%d' % id)
        #comment_form = CommentForm()

        # Updatd Comments:
'''


def update_comments(request, pk):
    context = {}
    obj = get_object_or_404(Comments, pk=pk)
    id = int(obj.post.pk)
    form = CommentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        #id = obj.post.pk
        # return redirect('/video_detail/', id)
        return HttpResponseRedirect('/video_detail/%d' % id)
    context = {
        'form': form,
        'obj': obj
    }
    return render(request, 'frontend/update_comments.html', context)


# Delete operation:
def delete_comments(request, pk):
    context = {}
    obj = get_object_or_404(Comments, pk=pk)
    id = int(obj.post.pk)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect('/video_detail/%d' % id)
    context = {
        'obj': obj
    }
    return render(request, "frontend/delete_comments.html", context)


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


@login_required
def subscription_view(request):
    context = {}
    channel_detail = ChannelInfo.objects.filter(
        subscribe=request.user)
    context = {
        'channel_detail': channel_detail
    }
    return render(request, 'frontend/subscription_view.html', context)


@login_required
def history_view(request):
    '''
    if request.method == "POST":
        user = request.user
        video = request.POST['history']
        history = HistoryInfo(video_info=video, user_name=user)
        history.save()
        return redirect(f'/video_detail/{video}')
    '''
    #channel_name = ChannelInfo.objects.all()
    #video_item = VideoInfo.objects.all()
    history = HistoryInfo.objects.filter(user_name=request.user)
    context = {
        # 'channel_name': channel_name,
        # 'video_item': video_item,
        'history': history
    }
    return render(request, 'frontend/history_view.html', context)
