from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 비워두었을 때 어디로 요청을 보내야 정상 작동할까?
    # articles/로 요청이 들어 왔을 때, index view 함수 실행, pattern name ='index'
    path('',views.index,name='index'),
    # new/create/
    # create/ -> GET create/ != POST create/
    path('create/', views.create, name='create'),
    # variable routing -> url converter : int,str,slug,uuid ...
    # 특정 게시글의 정보를 보여줄 detail 페이지를 만들 것이다
    # 특정값을 지정할 수 있는 unique 값은?
    # Primary Key -> integer
    # <값 정의 : 변수명>/
    path('<int:pk>/',views.detail, name='detail'),

    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/update/',views.update,name='update'),
    

]
