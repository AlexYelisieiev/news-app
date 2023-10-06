from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from . import forms

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', ]

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'age')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2', 'age')}),
    )


admin.site.register(models.CustomUser, CustomUserAdmin)
