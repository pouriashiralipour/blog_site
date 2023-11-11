from django.urls import path, re_path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='list_view'),
    path('comment/<int:article_id>', views.CommentsCreateView.as_view(), name='comment_view'),
    re_path(r'(?P<slug>[-\w]*)/$', views.ArticleDetailView.as_view(), name='details_view'),
    re_path(r'^category/(?P<slug>[-\w]*)/$', views.CategoryListView.as_view(), name='category_list_view'),
    path('tags/<int:pk>', views.TagsDetailsView.as_view(), name='tag_list_view')
    # path('category/', views.CategoryListView.as_view(), name='category_list_view'),

]
