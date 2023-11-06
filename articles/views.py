from django.shortcuts import render
from django.views import generic

from .models import Article


class ArticleListView(generic.ListView):
    template_name = 'articles/article_list_view.html'
    model = Article
    context_object_name = 'articles'


class ArticleDetailView(generic.DetailView):
    template_name = 'articles/article_detail_view.html'
    model = Article
