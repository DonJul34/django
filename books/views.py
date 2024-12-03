# views.py
from django.shortcuts import render
from .models import Book, Author, Genre
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
def delete_book(request, book_id):
    """
    Vue pour supprimer un livre.
    """
    book = get_object_or_404(Book, id=book_id)
    book_title = book.title  # Pour le message de confirmation
    book.delete()
    messages.success(request, f"Le livre '{book_title}' a été supprimé avec succès.")
    return redirect('book_list')  # Redirection vers la liste des livres


def book_list(request):
    # Récupération des filtres depuis l'URL
    title_query = request.GET.get('title', '')
    author_query = request.GET.get('author', '')
    year_query = request.GET.get('year', '')
    genre_query = request.GET.get('genre', '')
    sort_by = request.GET.get('sort_by', '')

    # Utilisation du manager pour appliquer les filtres
    books = Book.objects.filter_books(
        title=title_query,
        author=author_query,
        year=year_query,
        genre=genre_query,
        sort_by=sort_by
    )


    return render(request, 'books/book_list.html', {'books': books})