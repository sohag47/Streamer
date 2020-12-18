from django import forms
from dashboard.models import ChannelInfo, VideoInfo, Comments


class ChannelInfoForm(forms.ModelForm):
    class Meta:
        model = ChannelInfo
        fields = ('name', 'description', 'profile_img',
                  'cover_img', 'user_name')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Channel Name",
                    'required': 'true'

                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Channel Description",

                }
            ),
            'profile_img': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'cover_img': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'user_name': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'padding-top: 1px;'
                }
            )
        }


class VideoInfoForm(forms.ModelForm):
    class Meta:
        model = VideoInfo
        fields = ('title', 'description', 'video_content',
                  'video_img', 'channel_info', 'user_name')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Video Title",
                    'required': 'true'

                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Video Description",

                }
            ),
            'video_content': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'video_img': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'channel_info': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'padding-top: 1px;'
                }
            ),
            'user_name': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'padding-top: 1px;'
                }
            )
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Your Name",
                    'required': 'true'

                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Your Comment",

                }
            ),
        }
