from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms


# Create your views here.
class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.instance.age == None:
            form.instance.age = 0
        return super().form_valid(form)