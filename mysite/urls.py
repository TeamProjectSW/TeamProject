from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
   path('admin/', admin.site.urls),
   path('users/', include('users.urls')),
   path('', TemplateView.as_view(template_name='root.html'), name='root'),
]
