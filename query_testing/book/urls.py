from django.urls import path
from . import views

urlpatterns = [
    path('books1/', views.book_detail1, name='all_books_1'),
    path('books2/', views.book_detail2, name='all_books_2'),
    path('books3/', views.book_detail3, name='all_books_3'),

    path('ids1/', views.ids1, name='ids1'),
	path('ids2/', views.ids2, name='ids2'),
	path('ids3/', views.ids3, name='ids3'),
	path('ids4/', views.ids4, name='ids4'),
]