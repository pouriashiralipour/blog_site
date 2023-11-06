from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home_page.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'
