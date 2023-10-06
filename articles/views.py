from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models


# Create your views here.
class ArticleListView(LoginRequiredMixin, ListView):

    model = models.Article
    template_name = 'article_list.html'
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):

    model = models.Article
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = models.Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'
    login_url = 'login'

    def test_func(self):
        return self.get_object().author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, DeleteView):

    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin, CreateView):

    template_name = 'article_new.html'
    model = models.Article
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    template_name = 'comment_create.html'
    success_url = reverse_lazy('article_list')
    fields = ('comment',)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        form.instance.article = models.Article.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        return self.get_object().author == self.request.user
