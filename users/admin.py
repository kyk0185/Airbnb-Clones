from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['username','password','first_name','last_name','email','gender']}),
    ('Detail UserInfo',{'fields':['superhost','bio','is_staff','is_active']}),
    ('etc',{'fields':['is_superuser','date_joined','last_login']})]

    list_display = ('__str__','email','first_name','last_name','is_staff','gender',)

    list_filter = ('gender','is_staff')
