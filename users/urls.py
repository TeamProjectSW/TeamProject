from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
   path('login/', auth_views.LoginView.as_view(template_name='users/login_form.html'), name='login'),  ## 수정
   path('logout/', views.logout_view, name='logout'),
   path('signup/', views.signup, name='signup'),
   path('delete/', views.update, name='delete'),
   path('update/', views.update, name='update'),
]

