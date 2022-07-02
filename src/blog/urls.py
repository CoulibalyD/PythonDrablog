from django.urls import path

from .views import index, art

urlpatterns = [
    path('', index, name="blog-index"),
    path('art<str:article_number>/', art, name="blog-article_"),


]
