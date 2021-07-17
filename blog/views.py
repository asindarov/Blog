from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
# Create your views here.


class HomePageView(generic.TemplateView):
	template_name = 'blog/home.html'

class BlogListView(generic.ListView):
	template_name = 'blog/blog-list.html'
	queryset = Article.objects.all()

class BlogDetailView(generic.DetailView):
	template_name = 'blog/blog-detail.html'
	queryset = Article.objects.all()

class BlogCreateView(LoginRequiredMixin,generic.CreateView):
	form_class = ArticleForm
	template_name = 'blog/blog-create.html'
	def get_success_url(self):
		return reverse('blog-list')


class BlogUpdateView(LoginRequiredMixin,generic.UpdateView):
	form_class = ArticleForm
	template_name = 'blog/blog-update.html'
	queryset = Article.objects.all()
	def get_success_url(self):
		return reverse('blog-list')		

class BlogDeleteView(LoginRequiredMixin,generic.DeleteView):
	template_name = 'blog/blog-delete.html'
	queryset = Article.objects.all()
	
	def get_success_url(self):
		return reverse('blog-list')
