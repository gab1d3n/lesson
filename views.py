from django.shortcuts import render
from .forms import ProductForm

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid(): 
            form.save()  
            return render(request, 'product_created.html')  
        else:
            return render(request, 'create_product.html', {'form': form, 'error': 'Please correct the errors below.'})  # Ошибка валидации
    else:
        form = ProductForm()  
    return render(request, 'create_product.html', {'form': form})
