from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Create a FastAPI application instance
app = FastAPI()

# Define a Pydantic model for books


class Book(BaseModel):
    title: str
    author: str
    publication_year: int
    ISBN: str


# Initialize an empty list to store book data
books = []

# Create a book - POST request


@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    # Add the provided book to the list of books
    books.append(book)
    # Return the created book as the response
    return book

# Get all books - GET request


@app.get("/books/", response_model=List[Book])
async def get_books():
    return books  # Return the list of books as the response

# Get a specific book by ISBN - GET request


@app.get("/books/{ISBN}", response_model=Book)
async def get_book(ISBN: str):
    # Search for the book with the specified ISBN
    book = next((b for b in books if b.ISBN == ISBN), None)
    if book is None:
        # If book is not found, raise an HTTP 404 error
        raise HTTPException(status_code=404, detail="Book not found")
    return book  # Return the found book as the response


# Update a book by ISBN - PUT request
@app.put("/books/{ISBN}", response_model=Book)
async def update_book(ISBN: str, updated_book: Book):
    # Search for the book with the specified ISBN
    book = next((b for b in books if b.ISBN == ISBN), None)
    if book is None:
        # If book is not found, raise an HTTP 404 error
        raise HTTPException(status_code=404, detail="Book not found")

    # Update book details with the provided data
    for field in updated_book.dict(exclude_unset=True):
        setattr(book, field, getattr(updated_book, field))
    return book  # Return the updated book as the response


# Delete a book by ISBN - DELETE request
@app.delete("/books/{ISBN}", response_model=Book)
async def delete_book(ISBN: str):
    # Search for the book with the specified ISBN
    book = next((b for b in books if b.ISBN == ISBN), None)
    if book is None:
        # If book is not found, raise an HTTP 404 error
        raise HTTPException(status_code=404, detail="Book not found")

    # Remove the book from the list of books
    books.remove(book)
    return book  # Return the deleted book as the response

# Run the FastAPI application using Uvicorn if this script is the main program
if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI application on the specified host and port
    uvicorn.run(app, host="127.0.0.1", port=8090)
