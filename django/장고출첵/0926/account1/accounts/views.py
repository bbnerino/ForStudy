from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods,require_safe
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_safe
def index(request):
    return render(request,'accounts/index.html')

@login_required
def secret(request):
    user = request.user
    context={
        'user':user
    }
    return render(request,'accounts/secret.html',context)


@require_http_methods(['POST','GET'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:secret')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('accounts:secret')
    else:
        form = UserCreationForm()
    context ={
        'form':form 
    }
    return render(request,'accounts/signup.html',context)


@require_http_methods(['POST','GET'])
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:secret')

    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('accounts:secret')
    else:
        form = AuthenticationForm()
    context ={
        'form':form

    }
    return render(request,'accounts/login.html',context)

@login_required
@require_http_methods('POST')
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')