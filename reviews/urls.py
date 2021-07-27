from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("books", views.book_list, name="book_list"),
    path("books/", views.book_list, name="book_list"),
    # re_path(r"^/book-details/<int:id>/", views.book_details, name="book_details"),
    # path("book-details", views.book_details, name="book_details"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    # path("books/<int:pk>/", views.book_detail, name="book_detail"),
]
