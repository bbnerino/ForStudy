from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm
)

from django.views.decorators.http import require_POST, require_safe
#인증된 유저만 사용하는 데코
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm


User = get_user_model()
# ㄴ>현재 활성화된 유저 목록을 반환

@login_required
def index(request):
    # 모든 유저 목록을 보여주도록 할 것이다.
    # models Article.objects.all() (원래값)
    users= User.objects.all()
    context = {
        'users':users
    }
    return render(request,'accounts/index.html',context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    # 회원가입 시켜주세요-> DB에 정보 저장
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    # 회원가입 페이지 보여주세요 -> 문서 하나 보여주세요
    else: # GET
        form = UserCreationForm()
    context={
        'form':form
    }
    return render(request,'accounts/signup.html', context)

def login(request):
    # 이미 로그인한 유저라면
    if request.user.is_authenticated:
        return redirect('accounts:index')
    # 로그인 시켜줘
    if request.method =='POST':
        form= AuthenticationForm(request,request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request,form.get_user())
            
            return redirect(request.GET.get('next') or 'accounts:index')
    # 로그인 할 수 있는 페이지 보여줘
    else:
        form = AuthenticationForm()
    context ={
        'form':form
    }
    return render(request,'accounts/login.html',context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

@login_required
def update(request):
    # 수정해줘
    if request.method=="POST":
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    # 수정페이지
    else:
        form = CustomUserChangeForm(instance = request.user)
    context={
        'form':form
    }
    return render(request,'accounts/update.html',context)

def password_change(request):
    if request.method =="POST":
        form = PasswordChangeForm(request.user,data=request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
        
    else:
        form = PasswordChangeForm(request.user)
    context ={
        'form':form
    }
    return render(request,'accounts/password_change.html',context)