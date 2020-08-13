from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from src.models import UserProfile, ActivityPeriod

class UserProfileInline(admin.StackedInline):
	model = UserProfile


class ActivityPeriodInline(admin.TabularInline):
	model = ActivityPeriod
	extra = 4


class UserAdmin(BaseUserAdmin):
	inlines = (UserProfileInline, ActivityPeriodInline)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)