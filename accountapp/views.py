from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserSignupForm, AdminSignupForm, LoginForm
from .models import CustomUser
from django.contrib.auth import logout
from feedbackapp.models import Feedback
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    if request.user.is_admin:  
        all_feedback = Feedback.objects.select_related('user').order_by('-created_at')
        return render(request, 'accountapp/admin_dashboard.html', {'feedbacks': all_feedback})
    else:
        return redirect('landing')

def landing(request):
    return render(request, 'accountapp/landing.html')

def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            login(request, user)
            return redirect('feedback')
    else:
        form = UserSignupForm()
    return render(request, 'accountapp/user_signup.html', {'form': form})

def admin_signup(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = True
            user.save()
            login(request, user)
            return redirect('admin_dashboard')
    else:
        form = AdminSignupForm()
    return render(request, 'accountapp/admin_signup.html', {'form': form})

def user_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not CustomUser.objects.filter(username=username, is_user=True).exists():
            error = "Username not found!"
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_user:
                login(request, user)
                return redirect('feedback')
            else:
                error = "Invalid password!"

    return render(request, 'accountapp/user_login.html', {'form': LoginForm(), 'error': error})

def admin_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not CustomUser.objects.filter(username=username, is_admin=True).exists():
            error = "Admin username not found!"
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                error = "Invalid password!"

    return render(request, 'accountapp/admin_login.html', {'form': LoginForm(), 'error': error})

def user_logout(request):
    logout(request)
    return redirect('landing')
