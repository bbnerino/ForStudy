
import articles
from django.shortcuts import redirect, render,get_object_or_404
from .models import Article
from django.views.decorators.http import require_safe,require_POST
from .forms import ArticleForm
# Create your views here.

# GET 요청만 통과하도록 decorator를 사용한다.
@require_safe
def index(request):
    # 모든 게시물들을 보여줄 것.
    # 단, 내림차순으로 보여줄 것
    # 모델명.매니져.querysetAPI
    # <QuerySet [<Article Article object (1)>,...]
    articles = Article.objects.order_by('-pk')
    context = {
        'articles':articles
    }
    # render 함수의 2번째 인자 문자열 경로는 
    # 실제 파일이 저장되어 있는 경로를 의미하며, templates는 생략되어있다.
    return render(request,'articles/index.html',context)
    
def create(request):
    # 내가 작성한 데이터로 글 생성해줘
    # 사용자가 요청 보낸 방법을 이용해서 조건 분기
    if request.method == 'POST':
        #사용자가 요청 보낸 데이터는 어디에 있나?
        # 사용자가 요청 보낸 모든 정보는 request
        form = ArticleForm(request.POST,request.FILES)
        # 유효성 겁사:
        if form.is_valid():
            # 데이터를 db에 저장해야 pk가 생성된다
            # save 메서드의 반환값 해당 객체
            article = form.save()
            # 특정 문서를 반환하는 것이 아니라 다른경로로 보낼것이다.
            # redirect의 인자로 직접 경로를 작성해 줘도 정상 작동하지만 
            # app:pattern 형태로 사용할 수 있도록 하자
            # detail -> pk가 필요하다. article이 갖고 있는 pk를 넘겨준다
            # {% url 'articles:detail' article.pk %}
            # redirect 함수의 두번째 인자
            return redirect('articles:detail', article.pk)
    # 글 작성할 수 있는 페이지 보내줘
    else:
        # form이라고 하는 인스턴스를 만들어 줄 것이다.
        # form.py에서 정의한 ArticleForm 클래스의 인스턴스
        
        # print(form)-> html element 문자열 출력 -> 이것이 의미하는 바는?
        '''ModelForm의 매직매서드 __str__에는 
        model에 정의된 필드에 해당하는 label,input element의 형태를 만들어서
        출력하도록 설정되어있을 것이다.
        <label for="title">title: </label>
        -> context를 통해서 create.html 에게 넘겨 줬을때,
        {{form}}으로 출력하면 나오는 내용은?
        <label for="title">title: </label>
        {{article.title}} -> 제목
        __str__을 설정한 후, {{article}}-> 제목
        '''
        form = ArticleForm()
    context={
        'form':form
    }
    return render(request,'articles/create.html',context)
    # 글 작성할 수 있는 페이지 보여줘
    
def detail(request,pk):
    # 특정 게시물 하나를 보여줄 건데,
    # 만약 해당하는 게시물이 없으면 404 not found를 보여주도록 하고 싶다.
    # get_object_or_404는 어느 모델에 대한 조회인지 알 수 없다.
    article = get_object_or_404(Article, pk=pk)
    # Article.objects.get(pk=pk)->모델.매니져.쿼리셋
    context = {
        'article':article
    }
    return render(request,'articles/detail.html',context)

@require_POST
def delete(request,pk):
    # 요청이 POST일 떄만 삭제하도록 하고싶다.
    # POST 요청이 아니면 그냥 detail 문서에 남아있게 하고 싶다.
    # 특정 게시글 조회
    article = get_object_or_404(Article,pk=pk)
    
    # 게시글 삭제
    article.delete()
    return redirect('articles:index')
    # else:
    #     return redirect('articles:detail', article.pk)
def update(request,pk):
    article = get_object_or_404(Article,pk=pk)
    if request.method == "POST":
        # ModelForm(data=None,files=None,.... instance=None)
        # 기억안나면 print(help(ArticleForm))
        form =ArticleForm(request.POST,request.FILES,instance=article)
        if form.is_valid():
            article=form.save()
            return redirect('articles:detail',article.pk)
    else:
        # 단 수정을 하고자 할 때는
        # 어느 게시글을 수정하려고 하는 것인지
        # 처음 form 인스탄스 생성할때 같이 article의 정보
        # 넘겨주면서 생성할 것이다.
        form =ArticleForm(instance=article)
    context={
        'form':form
    }
    return render(request,'articles/update.html',context)