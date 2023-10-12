from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        obj = form.save()
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)



# def contacts(request):
#     return render(request, 'catalog/contacts.html')
class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    template_name = 'catalog/product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context['formset'] = formset
        return context

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
