from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render
from .models import Book
# api/views.py

from django.shortcuts import render, redirect
from .forms import BookForm




def book_list(request):
    # Fetch all books from the database
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book


def create_book(request):
    if request.method == 'POST':
        # Collect the data from the POST request
        title = request.POST.get('title')
        description = request.POST.get('description')
        published_date = request.POST.get('published_date')
        image = request.FILES.get('image')  # Handle image upload

        # Print the data to ensure it's coming through
        print("Form Data Received:")
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Published Date: {published_date}")
        print(f"Image: {image}")  # Ensure image is being received

        if title and description and published_date:
            # Create and save the book
            book = Book(
                title=title,
                description=description,
                published_date=published_date,
                image=image,
            )
            try:
                book.save()  # Save the book to the database
                print("Book saved successfully!")
            except Exception as e:
                print(f"Error saving book: {e}")
                return HttpResponse("Error saving book", status=500)

            # Redirect to book list page
            return redirect('book_list')
        else:
            print("Form validation failed.")
            return HttpResponse("All fields are required", status=400)

    return render(request, 'create_book.html')


def home(request):
    return redirect('book_list')