from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import Book

def list_books(request):
    books = Book.objects.all().values()  # This will get all books as dictionaries
    return JsonResponse(list(books), safe=False)

def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
        book_data = {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "published_date": book.published_date,
            "description": book.description,
            "page_count": book.page_count,
            "categories": book.categories,
            "thumbnail_url": book.thumbnail_url
        }
        return JsonResponse(book_data)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)


@csrf_exempt
def create_book(request):
    if request.method == "POST":
        data = request.POST
        try:
            book = Book.objects.create(
                title=data.get('title'),
                author=data.get('author'),
                published_date=data.get('published_date'),
                description=data.get('description'),
                page_count=data.get('page_count'),
                categories=data.get('categories'),
                thumbnail_url=data.get('thumbnail_url')
            )
            return JsonResponse({"id": book.id, "title": book.title})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

# Create your views here.
