from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from . import models

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = models.CustomUser
        fields = ('username', 'email', 'age')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = models.CustomUser
        fields = ('username', 'email', 'age')
