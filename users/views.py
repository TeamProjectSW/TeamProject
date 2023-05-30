from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, logout_then_login
from .forms import SignUpForm

def signup(request):
   if request.method == 'POST':
       form = SignUpForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, "회원가입을 환영합니다")
           return redirect("/")
   else:
       form = SignUpForm()
   return render(request, 'users/signup_form.html',{
       'form': form,
  })


login = LoginView.as_view(template_name="users/login_form.html")
def logout(request):
   return logout_then_login(request)