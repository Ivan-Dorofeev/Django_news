from django.urls import path

from app_news.views import NewsView, CreateNewsView, EditNewsView, NewsAndCommentsView, MainPage

urlpatterns = [
    path("", MainPage.as_view(), name='news'),
    path("news/", NewsView.as_view(), name='news'),
    path("news/create_news/", CreateNewsView.as_view(), name='create_news'),
    path("news/<int:pk>/edit_news/", EditNewsView.as_view(), name='edit_news'),
    path("news/<int:pk>/news_and_comments/", NewsAndCommentsView.as_view(), name='news_and_comments'),
]
