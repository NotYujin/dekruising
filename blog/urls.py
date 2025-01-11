from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main-page')
    # path('', views.post_list, name='post'),
    # path('', views.hero_list, name='hero'),
]