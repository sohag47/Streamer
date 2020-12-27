from django.contrib import admin
from dashboard.models import ChannelInfo, VideoInfo, Comments, HistoryInfo
# Register your models here.

# Register your models here.
# change admin header name
admin.site.site_title = "Admin Page"
admin.site.site_header = "Streamer Admin Panel"
admin.site.index_title = "Streamer"


class ChannelInfoAdmin(admin.ModelAdmin):
    #fields = ('name', 'user_name')
    #exclude = ('name', 'user_name')
    list_display = ('name',
                    'profile_img', 'cover_img', 'user_name', 'created_on')
    list_filter = ('name', 'user_name', 'created_on')
    search_fields = ('name', 'description')
    list_display_links = ('name', 'user_name', 'created_on')


admin.site.register(ChannelInfo, ChannelInfoAdmin)


class VideoInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'channel_info',
                    'video_content', 'video_img', 'user_name', 'updated')
    list_filter = ('title', 'channel_info', 'user_name', 'updated')
    search_fields = ('title', 'channel_info', 'description')
    list_display_links = ('title', 'user_name', 'updated')


admin.site.register(VideoInfo, VideoInfoAdmin)

admin.site.register(Comments)
admin.site.register(HistoryInfo)
