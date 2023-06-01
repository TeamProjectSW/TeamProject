from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
   #회원가입 폼 필수 필드 지정
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['user_id'].required = True
       self.fields['nick_name'].required = True
       self.fields['email'].required = True
       self.fields['phone_num'].required = True

   class Meta(UserCreationForm):
       model = User
       fields = ['user_id', 'nick_name', 'email', 'phone_num']



class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('nick_name','email','phone_num')

