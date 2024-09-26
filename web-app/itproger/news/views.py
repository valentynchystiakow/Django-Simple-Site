# import libraries(modules)
from typing import Type

from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
# import created models
from .models import Articles
# import created forms
from .forms import ArticlesForm


# news_home page view
def news_home(request):
    # orders all news objects by date
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


# Detail Article Page Class
class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


# Update Article Page Class
class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


# Delete Article Page Class
class NewsDeleteView(DeleteView):
    model = Articles
    # url which will redirect user after successful deleting of article
    success_url = '/news/'
    template_name = 'news/news-delete.html'


# Create new article page view
def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news')
        else:
            error = 'Form was invalid'
    form = ArticlesForm()
    data = {'form': form, 'error': error}
    return render(request, 'news/create.html', data)

