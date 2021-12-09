from django.shortcuts import redirect, render
from .models import Question
# Create
## 사용자가 데이터를 제출할 빈 html을 제공
def new(request):
    return render(request,'board/new.html')
## 사용자가 제출한 새로운 question을 저장
def create(request):
    question = Question()
    question.title = request.POST.get('title') # 키값 못찾아도 none 리턴 -> 오류 x
    question.category = request.POST.get('category') 
    question.content = request.POST.get('content') 
    question.save()
    return redirect('board:detail',question.pk)
    

# READ
## 전체 질문 목록 조회
def index(request):
    questions = Question.objects.all()
    context={
        'questions': questions
    }
    return render(request,'board/index.html',context)

## 단일 질문 상세 조회
def detail(request,question_pk):
    question = Question.objects.get(pk=question_pk)
    context ={
        'question':question,
    }
    return render(request,'board/detail.html',context)

# UPDATE
## 데이터를 제출할 기존 내용이 있는 html 제공
def edit(request,question_pk):
    question = Question.objects.get(pk=question_pk)
    context={
        'question':question
    }
    return render(request,'board/edit.html',context)

## 사용자가 제출한 데이터를 '기존 question'에 저장
def update(request,question_pk):
    question = Question.objects.get(pk=question_pk)
    question.title = request.POST.get('title') # 키값 못찾아도 none 리턴 -> 오류 x
    question.category = request.POST.get('category') 
    question.content = request.POST.get('content') 
    question.save()
    return redirect('board:detail',question.pk)
# DELETE
## 기존 question을 삭제
def delete(request,question_pk):
    question = Question.objects.get(pk=question_pk)

    if request.method == 'POST': 
        question.delete()
        return redirect('board:index')
    else:
        return redirect('board:index', question.pk)