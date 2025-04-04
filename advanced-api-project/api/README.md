# Advanced API Project - Testing Documentation

## Overview
This document provides an overview of the testing strategy and individual test cases for the `advanced_api_project`. The tests ensure the integrity of the API endpoints and the correctness of response data and status codes.

## Testing Strategy
The testing strategy focuses on the following key areas:
- CRUD operations for the Book model endpoints.
- Filtering, searching, and ordering functionalities.
- Permissions and authentication mechanisms.

## Test Cases

### Setup
The `setUp` method initializes the test client, creates a test user, author, and book, and logs in the test user.

### Test Create Book
- **URL:** `/api/books/create/`
- **Method:** `POST`
- **Description:** Creates a new book and verifies that the book is correctly saved and returned.
- **Assertions:**
  - Status code is `201 Created`.
  - Book count increases by 1.
  - The created book's title matches the provided data.

### Test Get Book List
- **URL:** `/api/books/`
- **Method:** `GET`
- **Description:** Retrieves the list of books and verifies the response data.
- **Assertions:**
  - Status code is `200 OK`.
  - The length of the response data matches the number of books in the database.
  - The retrieved book's title matches the expected data.

### Test Get Book Detail
- **URL:** `/api/books/<id>/`
- **Method:** `GET`
- **Description:** Retrieves the details of a single book by ID and verifies the response data.
- **Assertions:**
  - Status code is `200 OK`.
  - The retrieved book's title matches the expected data.

### Test Update Book
- **URL:** `/api/books/<id>/update/`
- **Method:** `PUT`
- **Description:** Updates an existing book and verifies that the changes are reflected.
- **Assertions:**
  - Status code is `200 OK`.
  - The updated book's title matches the provided data.

### Test Delete Book
- **URL:** `/api/books/<id>/delete/`
- **Method:** `DELETE`
- **Description:** Deletes a book and verifies that it is removed from the database.
- **Assertions:**
  - Status code is `204 No Content`.
  - Book count decreases by 1.

### Test Filter Books by Title
- **URL:** `/api/books/?title=<title>`
- **Method:** `GET`
- **Description:** Filters the list of books by title and verifies the response data.
- **Assertions:**
  - Status code is `200 OK`.
  - The length of the response data matches the number of books with the specified title.
  - The retrieved book's title matches the expected data.

### Test Search Books
- **URL:** `/api/books/?search=<search_term>`
- **Method:** `GET`
- **Description:** Searches for books by title or author name and verifies the response data.
- **Assertions:**
  - Status code is `200 OK`.
  - The length of the response data matches the number of books that match the search term.
  - The retrieved book's title matches the expected data.

### Test Order Books by Publication Year
- **URL:** `/api/books/?ordering=publication_year`
- **Method:** `GET`
- **Description:** Orders the list of books by publication year and verifies the response data.
- **Assertions:**
  - Status code is `200 OK`.
  - The books are ordered by publication year in ascending order.

## Running Tests
To run the tests, use the following command:

```sh
python manage.py test api
```

Review the outputs and fix any issues or bugs identified by the tests.