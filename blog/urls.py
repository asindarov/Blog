from django.urls import path
from . import views
urlpatterns = [
	path('', views.BlogListView.as_view(), name='blog-list'),
	path('<int:pk>/<slug:slug>', views.BlogDetailView.as_view(), name='blog-detail'),
	path('create/', views.BlogCreateView.as_view(), name='blog-create'),
	path('update/<int:pk>/<slug:slug>', views.BlogUpdateView.as_view(), name='blog-update'),
	path('delete/<int:pk>/<slug:slug>', views.BlogDeleteView.as_view(), name='blog-delete'),


]