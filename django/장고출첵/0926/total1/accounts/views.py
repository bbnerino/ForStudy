from accounts.forms import CustomUserChangeForm
from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods,require_POST
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.
User= get_user_model()

@require_http_methods(['POST','GET'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request,user)
            return redirect('articles:index')  
    else:
        form = UserCreationForm()
    context={
        'form':form
    }
    # return render(request,'accounts/signup.html',context)
    return render(request,'../../articles/templates/articles/form.html',context)

@require_http_methods(['POST','GET'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context ={
        'form':form
    }
    # return render(request,'accounts/login.html',context)
    return render(request,'../../articles/templates/articles/form.html',context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context ={
        'form':form
    }
    return render(request,'accounts/update.html',context)

@login_required
def index(request):
    users = User.objects.all()
    context ={
        'users':users
    }
    return render(request,'accounts/index.html',context)

@login_required
def password_change(request):
    if request.method =="POST":
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = PasswordChangeForm(request.user)
    context={
        'form':form
    }
    return render(request,'accounts/password_change.html',context)