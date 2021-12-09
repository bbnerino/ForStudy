from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods,require_POST,require_safe
from django.contrib.auth import get_user_model, login as auth_login , logout as auth_logout, get_user
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm

User = get_user_model()
# Create your views here.
def index(request):
    users=User.objects.all()
    context = {
        'users':users
    }
    return render(request,'accounts/index.html',context)

@require_http_methods(['POST','GET'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('accounts:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/form.html',context)

@require_http_methods(['POST','GET'])
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    if request.method =='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/form.html',context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('accounts:index')

@require_http_methods(['POST','GET'])
def update(request):
    user = request.user
    if request.method =='POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('accounts:index')
    else:
        form = UserChangeForm(instance=user)
    context = {
        'form':form
    }
    return render(request,'accounts/form.html',context)

@require_http_methods(['POST','GET'])
def change_password(request):
    user = request.user
    if request.method =='POST':
        form = PasswordChangeForm(user,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(user)
    context = {
        'form':form
    }
    return render(request,'accounts/form.html',context)

def delete(request):
    user = request.user
    user.delete()
    return redirect('accounts:index')
