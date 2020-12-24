from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import ExtraUserInfo


class SignUpForm(UserCreationForm):
    '''
    email = forms.CharField(max_length=254,
                            required=True,
                            widget=forms.EmailInput()
                            )
'''
    class Meta(object):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': "Enter Your First Name",
                    'required': 'true'

                }
            ),
            'last_name': forms.TextInput(
                attrs={

                    'placeholder': "Enter Your Last Name",
                    'required': 'true'

                }
            ),
            'username': forms.TextInput(
                attrs={

                    'placeholder': "Enter User Name ",
                    'required': 'true'

                }
            ),
            'email': forms.EmailInput(
                attrs={

                    'placeholder': "Enter Your Email",
                    'required': 'true'

                }
            ),
            'password1': forms.PasswordInput(
                attrs={

                    'placeholder': "Enter First Password",
                    'required': 'true'

                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'placeholder': "Enter Confirm Password",
                    'required': 'true'

                }
            ),
        }


# Login form
class LogInForm(AuthenticationForm):
    class Meta(object):
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter User Name",
                    'required': 'true'

                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Your Password",
                    'required': 'true'

                }
            ),
        }

# User Extra info form


class ExtraUserInfoForm(forms.ModelForm):
    class Meta:
        model = ExtraUserInfo
        fields = ('user_info', 'profile_img',
                  'country', 'language', 'description')
        widgets = {
            'user_info': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'padding-top: 1px;'
                }
            ),
            'profile_img': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'country': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter User Country",
                    'required': 'true'

                }
            ),
            'language': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter User Language",
                    'required': 'true'

                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Your Bio",

                }
            ),
        }
