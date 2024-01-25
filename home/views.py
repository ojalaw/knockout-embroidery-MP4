from django.shortcuts import render, redirect
from product.models import Product
from .forms import ContactForm
from django.contrib import messages

def home(request):
    products = Product.objects.all() 
    context = {
        'products': products,
    }
    return render(request, 'home/home.html', context)

def about_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('about_us')
        else:
            messages.error(request, 'There was an error with your form. Please check your information.')
    else:
        form = ContactForm()

    return render(request, 'home/about_us.html', {'form': form})