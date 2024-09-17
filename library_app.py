import tkinter as tk  # Import the tkinter library for GUI
from tkinter import messagebox  # Import the messagebox module for displaying pop-up messages
import sqlite3  # Import the sqlite3 library for database operations
from database_setup import initialize_db  # Import the initialize_db function to set up the database schema

class LibraryApp:
    def __init__(self, root):
        """
        Initialize the LibraryApp class. This sets up the main window and initializes the user interface components.
        
        :param root: The main Tkinter window.
        """
        self.root = root
        self.root.title("Library Management System")  # Set the title of the main window
        
        # Create the user interface widgets and load any necessary data
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        """
        Create and arrange the GUI components/widgets for the application.
        """
        # Frame for showing all books
        self.frame_show = tk.Frame(self.root)  # Create a frame to contain the "Show All Books" button
        self.frame_show.pack()  # Add the frame to the main window

        # Button to show all books
        self.show_button = tk.Button(self.frame_show, text="Show All Books", command=self.show_books)
        self.show_button.pack()  # Add the button to the frame

        # Frame for adding/editing a book
        self.frame_edit = tk.Frame(self.root)  # Create a frame to contain the input fields and buttons for book operations
        self.frame_edit.pack()  # Add the frame to the main window

        # Input fields and labels for book details
        tk.Label(self.frame_edit, text="Book Title").grid(row=0, column=0)
        self.entry_title = tk.Entry(self.frame_edit)
        self.entry_title.grid(row=0, column=1)

        tk.Label(self.frame_edit, text="Author").grid(row=1, column=0)
        self.entry_author = tk.Entry(self.frame_edit)
        self.entry_author.grid(row=1, column=1)

        tk.Label(self.frame_edit, text="ISBN").grid(row=2, column=0)
        self.entry_isbn = tk.Entry(self.frame_edit)
        self.entry_isbn.grid(row=2, column=1)

        tk.Label(self.frame_edit, text="Copies Purchased").grid(row=3, column=0)
        self.entry_copies_purchased = tk.Entry(self.frame_edit)
        self.entry_copies_purchased.grid(row=3, column=1)

        tk.Label(self.frame_edit, text="Copies Not Checked Out").grid(row=4, column=0)
        self.entry_copies_not_checked_out = tk.Entry(self.frame_edit)
        self.entry_copies_not_checked_out.grid(row=4, column=1)

        tk.Label(self.frame_edit, text="Retail Price").grid(row=5, column=0)
        self.entry_retail_price = tk.Entry(self.frame_edit)
        self.entry_retail_price.grid(row=5, column=1)

        # Button to add a new book
        self.add_button = tk.Button(self.frame_edit, text="Add Book", command=self.add_book)
        self.add_button.grid(row=6, column=0)

        # Button to edit an existing book
        self.edit_button = tk.Button(self.frame_edit, text="Edit Book", command=self.edit_book)
        self.edit_button.grid(row=6, column=1)

        # Button to remove a book
        self.remove_button = tk.Button(self.frame_edit, text="Remove Book", command=self.remove_book)
        self.remove_button.grid(row=6, column=2)

    def load_data(self):
        """
        Initialize the database if it doesn't already exist. This ensures the database and its schema are set up.
        """
        initialize_db()  # Call the imported function to set up the database schema

    def validate_input(self, title, author, isbn, copies_purchased, copies_not_checked_out, retail_price):
        """
        Validate the user input to ensure it meets the required format.

        :param title: Book title.
        :param author: Author's name.
        :param isbn: ISBN number of the book.
        :param copies_purchased: Number of copies purchased.
        :param copies_not_checked_out: Number of copies not checked out.
        :param retail_price: Retail price of the book.
        :return: True if all input is valid, False otherwise.
        """
        # Validate that the author's name contains only alphabetic characters
        if not author.isalpha():
            messagebox.showerror("Input Error", "Author must contain letters only.")
            return False
        
        # Validate that the ISBN is numeric
        if not isbn.isdigit():
            messagebox.showerror("Input Error", "ISBN must contain numbers only.")
            return False
        
        # Validate that the number of copies purchased and not checked out are integers
        if not (copies_purchased.isdigit() and copies_not_checked_out.isdigit()):
            messagebox.showerror("Input Error", "Number of copies must be integers.")
            return False
        
        # Validate that the retail price can be converted to a float
        try:
            float(retail_price)
        except ValueError:
            messagebox.showerror("Input Error", "Retail price must be a float.")
            return False
        
        return True

    def add_book(self):
        """
        Add a new book to the database using the provided input values.
        """
        # Retrieve input values from the entry fields
        title = self.entry_title.get()
        author = self.entry_author.get()
        isbn = self.entry_isbn.get()
        copies_purchased = self.entry_copies_purchased.get()
        copies_not_checked_out = self.entry_copies_not_checked_out.get()
        retail_price = self.entry_retail_price.get()

        # Validate the input values before adding the book
        if self.validate_input(title, author, isbn, copies_purchased, copies_not_checked_out, retail_price):
            # Connect to the SQLite database
            conn = sqlite3.connect('library.db')
            c = conn.cursor()
            # Execute the SQL command to insert the new book into the database
            c.execute('''
                INSERT INTO books (title, author, isbn, copies_purchased, copies_not_checked_out, retail_price)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (title, author, isbn, int(copies_purchased), int(copies_not_checked_out), float(retail_price)))
            # Commit the transaction to save the changes
            conn.commit()
            # Close the connection to the database
            conn.close()
            # Display a success message to the user
            messagebox.showinfo("Success", "Book added successfully!")

    def edit_book(self):
        """
        Edit the details of an existing book in the database.
        """
        # Retrieve input values from the entry fields
        isbn = self.entry_isbn.get()
        title = self.entry_title.get()
        author = self.entry_author.get()
        copies_purchased = self.entry_copies_purchased.get()
        copies_not_checked_out = self.entry_copies_not_checked_out.get()
        retail_price = self.entry_retail_price.get()

        # Validate the input values before updating the book
        if self.validate_input(title, author, isbn, copies_purchased, copies_not_checked_out, retail_price):
            # Connect to the SQLite database
            conn = sqlite3.connect('library.db')
            c = conn.cursor()
            # Execute the SQL command to update the book details in the database
            c.execute('''
                UPDATE books
                SET title = ?, author = ?, copies_purchased = ?, copies_not_checked_out = ?, retail_price = ?
                WHERE isbn = ?
            ''', (title, author, int(copies_purchased), int(copies_not_checked_out), float(retail_price), isbn))
            # Commit the transaction to save the changes
            conn.commit()
            # Close the connection to the database
            conn.close()
            # Display a success message to the user
            messagebox.showinfo("Success", "Book updated successfully!")

    def remove_book(self):
        """
        Remove a book from the database based on its ISBN.
        """
        # Retrieve the ISBN of the book to be removed
        isbn = self.entry_isbn.get()
        # Check if an ISBN has been provided
        if not isbn:
            messagebox.showerror("Input Error", "ISBN is required to remove a book.")
            return

        # Connect to the SQLite database
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        # Check if a book with the given ISBN exists
        c.execute('SELECT * FROM books WHERE isbn = ?', (isbn,))
        book = c.fetchone()
        # Close the connection to the database
        conn.close()

        # If the book exists, ask for confirmation before deleting it
        if book:
            confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the book with ISBN {isbn}?")
            if confirm:
                # Connect to the SQLite database
                conn = sqlite3.connect('library.db')
                c = conn.cursor()
                # Execute the SQL command to delete the book from the database
                c.execute('DELETE FROM books WHERE isbn = ?', (isbn,))
                # Commit the transaction to save the changes
                conn.commit()
                # Close the connection to the database
                conn.close()
                # Display a success message to the user
                messagebox.showinfo("Success", "Book removed successfully!")
        else:
            # Display an error message if no book with the given ISBN is found
            messagebox.showerror("Not Found", "No book found with the given ISBN.")

    def show_books(self):
        """
        Display all books in the database in a new window.
        """
        # Connect to the SQLite database
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        # Execute the SQL command to retrieve all books from the database
        c.execute('SELECT * FROM books')
        rows = c.fetchall()
        # Close the connection to the database
        conn.close()
        
        # If no books are found, display a message to the user
        if not rows:
            messagebox.showinfo("Books", "No books found.")
            return
        
        # Create a new window to display the list of books
        show_window = tk.Toplevel(self.root)
        show_window.title("All Books")
        # Display each book's details in the new window
        for row in rows:
            tk.Label(show_window, text=row).pack()

# Main execution: create the main Tkinter window and start the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window
    app = LibraryApp(root)  # Instantiate the LibraryApp class
    root.mainloop()  # Start the Tkinter event loop
