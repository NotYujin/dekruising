from django.shortcuts import render
from .forms import ClientMessageForm
from .models import *

def main_page(request):
    if request.method == 'POST':
        form = ClientMessageForm(request.POST)
        if form.is_valid():
            form.save()  # Automatically saves the data to the database
            success = True
            hero_main = HeroList.objects.filter(main_hero=True).first()
            posts = Post.objects.order_by('-created_date')
            products = Product.objects.all()
            return render(request, 'blog/base.html', {
                'hero_main': hero_main,
                'posts': posts,
                'products': products,
                'form': ClientMessageForm(),
                'success': success
            })
    else:
        form = ClientMessageForm()

    hero_main = HeroList.objects.filter(main_hero=True).first()
    posts = Post.objects.order_by('-created_date')
    products = Product.objects.all()
    return render(request, 'blog/base.html', {
        'hero_main': hero_main,
        'posts': posts,
        'products': products,
        'form': form
    })
