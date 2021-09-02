from django.urls import path
from . import views


from .views import NewsListView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_home'),
    path('add_article', views.add_article, name='add_article'),
]