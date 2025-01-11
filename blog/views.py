from django.shortcuts import render
from .models import *

# def post_list(request):
#     posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
#     return render(request, 'blog/base.html', {'posts' : posts})

# def hero_list(request):
#     heros = Hero.objects.filter(main_hero=True).first()
#     return render(request, 'blog/base.html', {'heros': heros})

def main_page(request):
    hero_main = HeroList.objects.filter(main_hero=True).first()
    posts = Post.objects.order_by('-created_date')
    products = Product.objects.all()
    return render(request, 'blog/base.html', {'hero_main': hero_main,
                                                'posts': posts,
                                                'products': products})