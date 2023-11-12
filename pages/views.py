from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .models import ContactUsModel
from .forms import NewsEmailForm
from articles.models import Article, Category


def home_page_view(request):
    offer_article = Article.objects.filter(status='p', offer_article=True).order_by('-publish')[1:]
    last_offer_article = Article.objects.filter(status='p', offer_article=True).order_by('-publish')[:1]
    hottest_article = Article.objects.filter(status='p', hottest_article=True).order_by('-publish')[:1]
    favorite_article = Article.objects.filter(status='p').annotate(like_count=models.Count('likes')).order_by(
        '-like_count')
    favorite_article_index1 = Article.objects.filter(status='p').annotate(like_count=models.Count('likes')).order_by(
        '-like_count')[:1]
    favorite_article_index2 = Article.objects.filter(status='p').annotate(like_count=models.Count('likes')).order_by(
        '-like_count')[1:2]
    favorite_article_index3 = Article.objects.filter(status='p').annotate(like_count=models.Count('likes')).order_by(
        '-like_count')[2:4]
    favorite_article_index4 = Article.objects.filter(status='p').annotate(like_count=models.Count('likes')).order_by(
        '-like_count')[4:6]
    articles = Article.objects.filter(status='p').order_by('-publish')
    category = Category.objects.filter(active=True).order_by('-datetime_created')

    if request.method == 'POST':
        news_form = NewsEmailForm(request.POST)
        if news_form.is_valid():
            new_form = news_form.save(commit=False)
            new_form.save()
    else:
        news_form = NewsEmailForm
    context = {'articles': articles,
               'hottest_article': hottest_article, 'category': category, 'form': news_form,
               'offer_article': offer_article, 'last_offer_article': last_offer_article,
               'favorite_article': favorite_article, 'favorite_article_index1': favorite_article_index1,
               'favorite_article_index2': favorite_article_index2, 'favorite_article_index3': favorite_article_index3,
               'favorite_article_index4': favorite_article_index4}
    return render(request, 'pages/home_page.html', context)


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


class ContactUsView(CreateView):
    template_name = 'pages/contact_us.html'
    model = ContactUsModel
    fields = ['name', 'email', 'topic', 'text']
    success_url = reverse_lazy('pages:contact_us')
