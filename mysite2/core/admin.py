from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,	{'fields': ['username', 'age',
			'education', 'is_active', 'is_staff']})]
			

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
