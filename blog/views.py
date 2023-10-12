from django.core.mail import send_mail
from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog
from config import settings


class BlogListView(ListView):
    model = Blog


def get_queryset(self, *args, **kwargs):
    queryset = super().get_queryset(*args, **kwargs)
    queryset = queryset.filter(is_published=True)
    return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.views_count += 1
        obj.save()
        return obj


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'content', 'image', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'content', 'image', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
