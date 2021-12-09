### PJT06

![image-20210917170259669](README.assets/image-20210917170259669.png)

로그인 관련된 내용이 추가된 프로젝트였다.

```python
@require_http_methods(['POST','GET'])
def login(request): 
    if request.user.is_authenticated: 
        return redirect('community:index') 
    if request.method =='POST': # 
        form = AuthenticationForm(request, request.POST) 
        # from django.contrib.auth.forms import AuthenticationForm
        # 으로 AuthenticationForm 을 받아와
        if form.is_valid(): # 유효성 검사가 되면
            auth_login(request, form.get_user()) # 로그인을 한다 -> 
            # from django.contrib.auth import login as auth_login 으로 이름바꾸기
            return redirect(request.GET.get('next') or 'community:index')
        
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)
```

## 로그인

if  로그인이 되어있다

​	> 전체 조회페이지

if request로 POST를 받았으면

​	form 은 인증form에서 POST로 들어온것

​	유효성 검사 

​		>  로그인을 한다 . get_user

else POST가 아니면

​	form 은 빈값

```python
@require_http_methods(['POST','GET'])
def signup(request):
    if request.user.is_authenticated:
        return redirect("community:index")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('community:index')
    else:
        form = UserCreationForm()
    context ={
        'form':form
    }
    return render(request,'accounts/signup.html',context)
```

## 회원가입하기

로그인 되어있으면?

​	> 인덱스창으로

request의 값이 POST이면

​	> UserCreationForm을 이용한다

​	> 유효성 검사

​		>> user에 form값을 저장하고

​		>>  user로 로그인

```python
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        # from django.contrib.auth import logout as auth_logout
    return redirect('community:index')
```

로그인 되어있다면

​	> 로그아웃하기

​	