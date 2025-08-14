from django.urls import path
from app.views.books import *

urlpatterns = [
    # Book URLs
    path('', book_list, name='book-list'),
    path('<int:pk>/detail', book_detail, name='book-detail'),
    path('new/', book_create, name='book-create'),
    path('<int:pk>/edit/', book_update, name='book-update'),
    path('<int:pk>/delete/', book_delete, name='book-delete')

]