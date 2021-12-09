from django.urls import path
from . import views
# /board/ + ?
app_name = "board"
urlpatterns = [
    path('new/',views.new,name='new'),
    path('create/',views.create,name='create'),
    path('',views.index,name='index'),
    path('<int:question_pk>/',views.detail,name='detail'),
    path('<int:question_pk>/edit',views.edit,name='edit'),
    path('<int:question_pk>/update',views.update,name='update'),
    path('<int:question_pk>/delete',views.delete,name='delete'),

]
"""
C
/board/new/
/board/create/
R
/board/
/board/1/
U 
/board/1/edit
/board/1/update/
D
/board/1/delete
"""