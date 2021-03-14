from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from app_news.forms import NewsForm
from app_news.models import News


class MainPage(View):

    def get(self, request):
        return render(request, 'main.html', {})


class NewsView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_data'


class CreateNewsView(CreateView):
    template_name = 'create_news.html'
    form_class = NewsForm
    success_url = '/news/'


class EditNewsView(UpdateView):
    model = News
    template_name = 'edit_news.html'
    form_class = NewsForm
    success_url = '/news/'


class NewsAndCommentsView(DetailView):
    model = News
    template_name = 'news_and_comments.html'
    context_object_name = 'news_data'
