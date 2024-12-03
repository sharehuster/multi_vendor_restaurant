from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',)
    
    # here is 3 command for noneditable password
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, CustomUserAdmin)
#show view class user of model  /admin

admin.site.register(UserProfile)
