from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
# 사용하고 있는 모델을 사용하여 참조해야한다

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields =('email','first_name','last_name',)