from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .models import ContactUsModel


class HomePageView(TemplateView):
    template_name = 'pages/home_page.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


class ContactUsView(CreateView):
    template_name = 'pages/contact_us.html'
    model = ContactUsModel
    fields = ['name', 'email', 'topic', 'text']
    success_url = reverse_lazy('pages:contact_us')
