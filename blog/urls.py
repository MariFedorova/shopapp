from django.urls import path

from blog.apps import BlogConfig

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),

]
