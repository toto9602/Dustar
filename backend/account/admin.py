from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

admin.site.register(User)


# class ProfileInline(admin.StackedInline):
#     model = Profile
#     verbose_name_plural = 'profile'

# class UserAdmin(BaseUserAdmin):
#     inlines = [ProfileInline, ]

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

# admin.site.register(Profile)