from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext, gettext_lazy as _

from .models import Article, Comments, Category
from .forms import CommentForm


class ArticleListView(generic.ListView):
    template_name = 'articles/article_list_view.html'
    model = Article
    context_object_name = 'articles'


class ArticleDetailView(generic.DetailView):
    template_name = 'articles/article_detail_view.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CommentsCreateView(SuccessMessageMixin, generic.CreateView):
    model = Comments
    form_class = CommentForm
    success_message = _('Your comment was successfully registered.')

    def form_valid(self, form):
        obj = form.save(commit=False)
        # obj.user = self.request.user

        article_id = int(self.kwargs['article_id'])
        article = get_object_or_404(Article, id=article_id)
        obj.article = article

        return super().form_valid(form)


class CategoryListView(generic.DetailView):
    template_name = 'articles/category.html'
    model = Category
    context_object_name = 'category'


def category_detail_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(status='p').order_by('-publish')
    context = {
        'category': category,
        'articles': articles,
    }
    return render(request, 'articles/category.html', context)
