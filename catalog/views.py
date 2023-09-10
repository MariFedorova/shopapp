from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    context = {
        'objects_list': Product.objects.all(),
        'title': 'Каталог'
    }
    return render(request, 'catalog/home.html', context)


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')
