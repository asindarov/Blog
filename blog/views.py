from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.


class BlogListView(generic.ListView):
	template_name = 'blog/blog-list.html'
	queryset = Article.objects.all()