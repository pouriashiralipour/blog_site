from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('', views.AboutUsView.as_view(), name='about_us'),
    path('', views.ContactUsView.as_view(), name='contact_us'),
]
