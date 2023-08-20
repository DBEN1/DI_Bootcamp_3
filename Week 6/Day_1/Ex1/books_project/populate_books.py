import os
import requests
from django.core.wsgi import get_wsgi_application

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_project.settings')
application = get_wsgi_application()

from books.models import Book

def fetch_books_from_google(query):
    GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes?q={}"
    response = requests.get(GOOGLE_BOOKS_API_URL.format(query))
    
    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        print(f"Error fetching books: {response.status_code}")
        return []


def save_books_to_model(books_data):
    for book_data in books_data:
        volume_info = book_data.get('volumeInfo', {})
        
        # Handle the published_date format
        published_date = volume_info.get('publishedDate', None)
        if published_date:
            if len(published_date) == 4:  # If only the year is provided
                published_date += "-01-01"  # Default to January 1st of that year
        
        Book.objects.create(
            title=volume_info.get('title', 'Unknown Title'),
            author=", ".join(volume_info.get('authors', ['Unknown Author'])),
            published_date=published_date,
            description=volume_info.get('description', ''),
            page_count=volume_info.get('pageCount', 0),
            categories=", ".join(volume_info.get('categories', [])),
            thumbnail_url=volume_info.get('imageLinks', {}).get('thumbnail', '')
        )

if __name__ == "__main__":
    query = input('Enter search terms for books (e.g., python, django) ')
    books_data = fetch_books_from_google(query)
    save_books_to_model(books_data)
    print(f'Added {len(books_data)} books to the database!')
