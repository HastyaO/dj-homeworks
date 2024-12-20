from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_obj = Phone.objects.all()
    sort_value = request.GET.get('sort')
    if sort_value == 'min_price':
        phone_obj = phone_obj.order_by('price')
    elif sort_value == 'max_price':
        phone_obj = phone_obj.order_by('-price')
    elif sort_value == 'name':
        phone_obj = phone_obj.order_by('name')
    context = {
        'phones': phone_obj,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone =  get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)