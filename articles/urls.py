from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(),
         name='article_detail'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(),
         name='article_edit'),
    path('new/', views.ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(),
         name='article_delete'),
    path('comment/<int:pk>/create/', views.CommentCreateView.as_view(),
         name='comment_create'), # pk - article's personal key
     path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(),
         name='comment_delete') # pk - comment's personal key
]
