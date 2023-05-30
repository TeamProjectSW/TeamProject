from django.contrib.auth.forms import UserCreationForm
from .models import User

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

