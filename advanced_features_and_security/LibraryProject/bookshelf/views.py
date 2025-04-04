from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from .models import Book
from .forms import ExampleForm
from .forms import BookForm
from django.db.models import Q

@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    query = request.GET.get("q", "").strip()
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@login_required
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})

@login_required
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.user.has_perm('bookshelf.can_edit'):
        if request.method == "POST":
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect("book_list")
        else:
            form = BookForm(instance=book)
        return render(request, "bookshelf/book_form.html", {"form": form})
    return HttpResponseForbidden("You don't have permission to edit this book.")

@login_required
@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST" and request.user.has_perm('bookshelf.can_delete'):
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})

