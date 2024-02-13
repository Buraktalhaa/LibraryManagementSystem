# LibraryManagementSystem
This project is an assignment given as part of the Akbank Python Bootcamp. The objective of this project is to develop a Library Management System using object-oriented programming techniques. The program utilizes a file named "books.txt" as its database, where each line represents a single book with details such as the book name, author, release date, and number of pages separated by commas.
## Usage

1. **Creating the Library Class**  
   The Library class consists of a constructor method responsible for opening the "books.txt" file and a destructor method to close the file.

2. **Library Methods**  
   - **List Books**: This method lists all the books stored in the "books.txt" file. It reads the contents of the file, splits each line using the splitlines() method, and stores them in a list. Each element in the list contains information about a single book, from which the book name and author are extracted and printed to the screen.  
   - **Add Book**: This method adds a new book to the "books.txt" file. It prompts the user for details such as the book title, author, first release year, and number of pages, creates a string with this information, and appends it as a new line to the file.  
   - **Remove Book**: This method deletes a book with the specified title from the "books.txt" file. It prompts the user for the book title, reads the contents of the file, removes the specified book from the list, clears the contents of the file, and writes the updated book list back to the file.

3. **Creating the Menu**
   - The user is presented with the following menu options:
     ```
     *** MENU***
     1) List Books
     2) Add Book
     3) Remove Book
     ```
   - The user selects a menu item and the relevant method of the `lib` object is called.
## Contribution

Contributions to this project are welcome. If you wish to contribute, please start by opening an issue or submitting a pull request. Please provide a detailed description of the proposed changes.

## Assignment Requirements

You can download the PDF document containing the assignment requirements from [here](link_to_the_pdf_document).


