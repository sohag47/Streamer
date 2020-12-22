import django_filters
from django_filters import CharFilter
from dashboard.models import ChannelInfo, VideoInfo


class VideoFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = VideoInfo
        fields = ['title']
