from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .models import ContactUsModel
from articles.models import Article, Category


# class HomePageView(TemplateView):
#     template_name = 'pages/home_page.html'
def home_page_view(request):
    # offer_article = Article.objects.filter(status='p', offer_article=True).order_by('-publish')[1:]
    # last_offer_article = Article.objects.filter(status='p', offer_article=True).order_by('-publish')[:1]
    hottest_article = Article.objects.filter(status='p').order_by('-publish')[:1]
    articles = Article.objects.filter(status='p').order_by('-publish')
    category = Category.objects.filter(active=True).order_by('-datetime_created')
    context = {'articles': articles,
               'hottest_article': hottest_article, 'category': category}
    return render(request, 'pages/home_page.html', context)


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


class ContactUsView(CreateView):
    template_name = 'pages/contact_us.html'
    model = ContactUsModel
    fields = ['name', 'email', 'topic', 'text']
    success_url = reverse_lazy('pages:contact_us')
