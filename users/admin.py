from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
   list_display = (
       'user_id',
       'nick_name',
       'email',
       'phone_num',
      )
   search_fields = ('user_id', 'nick_name', 'phone_num')

admin.site.register(User, UserAdmin)
admin.site.unregister(Group) #Group삭제 부분