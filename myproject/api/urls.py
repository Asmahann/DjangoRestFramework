from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('create-book/', views.create_book, name='create_book'),
]
