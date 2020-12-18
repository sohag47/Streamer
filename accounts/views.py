from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from accounts.forms import SignUpForm
# Create your views here.


# Create Account:
def signup(request):
    if(request.method == 'POST'):
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
