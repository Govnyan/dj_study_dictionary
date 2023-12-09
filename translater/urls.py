from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('/', views.home, name='home'),
    path('words_list', views.read_from_file, name='read_from_file'),
    path('words_list/', views.read_from_file, name='read_from_file'),
    path('add_word', views.add_word, name='add_word'),
    path('add_word/', views.add_word, name='add_word'),
]
