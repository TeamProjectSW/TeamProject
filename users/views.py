from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm

def signup(request):
   if request.method == 'POST':
       form = SignUpForm(request.POST)
       if form.is_valid():
           form.save()
           nick_name = form.cleaned_data.get('nick_name')  ##추가
           user = authenticate(username=nick_name)  ##추가
           login(request, user)  ##추가
           return redirect("root")  ##수정
   else:
       form = SignUpForm()
   return render(request, 'users/signup_form.html',{
       'form': form,
  })


login = LoginView.as_view(template_name="users/login_form.html")
def logout_view(request):  ##수정
    logout(request)       ##수정
    return redirect("root")    ##수정




# 탈퇴
from django.views.decorators.http import require_POST
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth.logout(request)
    return redirect('layout.html')


# 수정
from .forms import CustomUserChangeForm
from django.contrib.auth.views import login_required
from django.views.decorators.http import require_http_methods
@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "수정되었습니다")
            return redirect("/")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }

    return render(request, 'users/mypage.html', context)

