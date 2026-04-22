from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product, PreOrder
from .forms import PreOrderForm


def product_list(request):
    products = Product.objects.filter(is_active=True)
    selected_brand = request.GET.get('brand', '')

    if selected_brand:
        products = products.filter(brand=selected_brand)

    # FIX 5: pass full BRAND_CHOICES list so all tabs render
    brand_choices = Product.BRAND_CHOICES

    return render(request, "product/product_list.html", {
        "products": products,
        "brand_choices": brand_choices,
        "selected_brand": selected_brand,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)

    if request.method == "POST":
        form = PreOrderForm(request.POST, product=product)
        if form.is_valid():
            preorder = form.save(commit=False)
            preorder.product = product
            preorder.save()
            return redirect(reverse("preorder_thanks", args=[preorder.id]))
    else:
        form = PreOrderForm(product=product)

    return render(request, "product/product_detail.html", {
        "product": product,
        "form": form,
    })


def preorder_thanks(request, pk):
    return render(request, "product/preorder_thanks.html", {"preorder_id": pk})