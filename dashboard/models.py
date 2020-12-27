from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ChannelInfo(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    profile_img = models.ImageField(null=True, blank=True, upload_to='images/')
    cover_img = models.ImageField(null=True, blank=True, upload_to='images/')
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribe = models.ManyToManyField(
        User, blank=True, related_name='subscribe_channel')

    def __str__(self):
        return self.name

    def total_subscriber(self):
        return self.subscribe.count()


class VideoInfo(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    video_content = models.FileField(
        null=True, blank=True, upload_to='videos/')
    video_img = models.ImageField(null=True, blank=True, upload_to='images/')
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    channel_info = models.ForeignKey(ChannelInfo, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, blank=True, related_name='video_post')
    view = models.IntegerField(default=0, null=0, blank=True)
    keyword = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.like.count()

    def total_video(self):
        return self.video_content.count()


# Video Hostory:
class HistoryInfo(models.Model):
    video_info = models.ForeignKey(VideoInfo, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)


# Comments:
class Comments(models.Model):
    post = models.ForeignKey(
        VideoInfo, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
