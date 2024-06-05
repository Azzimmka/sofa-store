from django.shortcuts import render, redirect

from my_app1.models import PopularProduct, Newsletter
from .forms import Contact, ContactForm, NewsletterForm


def index(request):
    context = {
        'title': ' index',
        'products': PopularProduct.objects.all(),
    }
    return render(request, 'my_app1/index.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def about(request):
    return render(request, 'about.html')


def shop(request):
    return render(request, 'shop.html')


def services(request):
    return render(request, 'services.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def cart(request):
    return render(request, 'cart.html')
