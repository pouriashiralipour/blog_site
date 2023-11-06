from django.urls import path, re_path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='list_view'),
    re_path(r'(?P<slug>[-\w]*)/$', views.ArticleDetailView.as_view(), name='details_view'),
]
