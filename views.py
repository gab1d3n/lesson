from django.shortcuts import render
from .forms import ProductForm, IceCreamForm

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'product_created.html')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def create_ice_cream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ice_cream_created.html')
    else:
        form = IceCreamForm()
    return render(request, 'create_ice_cream.html', {'form': form})
