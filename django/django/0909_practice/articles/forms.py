from django import forms
from .models import Article

# Form에는 두가지 종류가 있는데,
# Model에 대한 정보의 유무를 기준으로 나눈다.
# Model에 대한 정보가 없는 Form의 경우는 내가 직접 Field들을 정의 해야한다.
# ModelForm은 모델에 대한 정보를 기입해주기 때문에, 직접적으로 Field를 정의하지 않아도 된다.
# 추가 설정이나 속성등은 ModelForm도 widget을 통해 설정 가능하다.
class ArticleForm(forms.ModelForm):
    # Model에 대한 정보를 기입할 수 있는 방법은?
    # class에 대한 정보
    class Meta:
        model = Article
        # fields = ('title','content','image',)
        fields = '__all__'
