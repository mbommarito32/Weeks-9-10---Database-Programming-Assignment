import sqlite3  # Import the sqlite3 library for database operations

def initialize_db():
    """
    Create the database and the necessary tables if they do not already exist.
    This function sets up the 'books' table with appropriate columns.
    """
    # Connect to the SQLite database file; create it if it does not exist
    conn = sqlite3.connect('library.db')
    
    # Create a cursor object to execute SQL commands
    c = conn.cursor()
    
    # Execute SQL command to create the 'books' table if it does not exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for each book, auto-incremented
            title TEXT NOT NULL,  -- Title of the book, cannot be null
            author TEXT NOT NULL,  -- Author of the book, cannot be null
            isbn TEXT NOT NULL UNIQUE,  -- ISBN of the book, unique and cannot be null
            copies_purchased INTEGER NOT NULL,  -- Number of copies purchased, cannot be null
            copies_not_checked_out INTEGER NOT NULL,  -- Number of copies not checked out, cannot be null
            retail_price REAL  -- Retail price of the book, can be null (optional)
        )
    ''')
    
    # Commit the transaction to save changes to the database
    conn.commit()
    
    # Close the connection to the database
    conn.close()

# If this script is executed directly (not imported as a module), initialize the database
if __name__ == "__main__":
    initialize_db()  # Call the function to set up the database and tables
