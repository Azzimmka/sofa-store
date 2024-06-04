from django.shortcuts import render, redirect
from .forms import Contact, ContactForm
from .models import ShopProduct


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')




def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')


def detail(request):
    return render(request, 'product_detail.html')




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



def shop(request):
    product = ShopProduct.objects.all()
    return render(request, 'shop.html', {'product':product})

def product_detail(request, slug):
    products = ShopProduct.objects.get(slug__iexact=slug)
    return render(request, 'product_detail.html', {'products': products})


