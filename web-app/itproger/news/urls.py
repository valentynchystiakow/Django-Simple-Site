# import libraries(modules)
from django.urls import path

# import views
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    # news/1,2,3 ...
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    # news/1/update
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    # news/1/delete
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
]
