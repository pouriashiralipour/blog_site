from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about_us/', views.AboutUsView.as_view(), name='about_us'),
    path('contact_us', views.ContactUsView.as_view(), name='contact_us'),
]
