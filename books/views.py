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
    books = Book.objects.all()

    # Récupération des filtres et paramètres de tri depuis l'URL
    title_query = request.GET.get('title', '')
    author_query = request.GET.get('author', '')
    year_query = request.GET.get('year', '')
    genre_query = request.GET.get('genre', '')
    sort_by = request.GET.get('sort_by', '')

    # Filtres conditionnels
    if title_query:
        books = books.filter(title__icontains=title_query)
    if author_query:
        books = books.filter(author__name__icontains=author_query)
    if year_query.isdigit():
        books = books.filter(publication_year__gte=int(year_query))  # Années après une certaine date
    if genre_query:
        books = books.filter(genres__name__icontains=genre_query)

    # Tri dynamique
    if sort_by in ['title', 'author__name', 'publication_year']:
        books = books.order_by(sort_by)

    return render(request, 'books/book_list.html', {'books': books})