from django.shortcuts import render, redirect
from .forms import Contact, ContactForm


def index(request):
    return render(request, 'index.html')


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





def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

