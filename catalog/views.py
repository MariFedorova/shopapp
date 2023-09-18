from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from catalog.models import Product


# Create your views here.
def home(request):
    context = {
        'objects_list': Product.objects.all(),
        'title': 'Каталог'
    }
    return render(request, 'catalog/home.html', context)


# def product(request, pk):
# context = {
# 'object': Product.objects.get(pk=pk)
# }
# return render(request, 'catalog/product_detail.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

class ProductDetailView(DetailView):
    model = Product
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(product_id=self.kwargs.get('pk'))
    #     return queryset
    #
    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['object'] = Product.objects.get(pk=pk)
    #
    #     return context_data

class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'price', 'category')
    success_url = reverse_lazy('catalog:home')


# def contacts(request):
#     return render(request, 'catalog/contacts.html')
class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'