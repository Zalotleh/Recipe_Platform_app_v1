from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm


def store_page(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {'products': products, 'category': category, 'categories': categories}
    return render(request, 'store/product/store.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Products, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'store/product/product_detail.html',
                  {'product': product, 'cart_product_form': cart_product_form}
                  )
