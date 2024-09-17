# Library Management System

## Overview
This project is a simple library management system using Python with Tkinter for the GUI and SQLite for database storage.

## Files
- `database_setup.py`: Initializes the SQLite database.
- `library_app.py`: Main application script with GUI and CRUD operations.
- `library.db`: SQLite database file (created automatically).
- `README.md`: Project documentation.

## Setup
1. Run `database_setup.py` to create the database:
   ```bash
   python database_setup.py
   ```
2. Run `library_app.py` to start the application:
   ```bash
   python library_app.py
   ```

## Usage
- **Show All Books**: Display all books in the library.
- **Add Book**: Add a new book with title, author, ISBN, copies purchased, copies not checked out, and retail price.
- **Edit Book**: Update details of an existing book using its ISBN.
- **Remove Book**: Delete a book by its ISBN.
