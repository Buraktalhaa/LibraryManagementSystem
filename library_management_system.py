
class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def listBooks(self):
        with open("books.txt", "r") as file:
            lines = file.read().splitlines()

            for line in lines:
                book_information = line.strip().split(",")
                book_name = book_information[0]
                author = book_information[1]
                release_date = book_information[2]
                number_of_pages = book_information[3]
                print(f"Book name: {book_name},Author name: {author}")

    def addBook(self,book, author, release_date, number_of_pages):
        with open("books.txt", "a") as dosya:
            dosya.write(f"{book},{author},{release_date},{number_of_pages}\n")


    def removeBook(self,book_name):
        with open("books.txt", "r") as file:
            lines = file.readlines()            

        found = False
        with open("books.txt", "w") as file:
            for line in lines:
                if book_name.strip() != line.split(',')[0].strip():        
                    file.write(line)
                else:
                    found = True

        if found:
            print(f"{book_name} was deleted successfully.")
        else:
            print(f" The book named {book_name} was not found.")

while True:
    print(" ")
    print("***MENU***")
    print("1)List Books")
    print("2)Add Book")
    print("3)Remove Book")
    print("4)Quit")
    
    selection = input("Please select the action you want to perform: ")
    
    lib = Library()

    if selection == "1":
        lib.listBooks()

    elif selection == "2":    
        selection1 = input("Please enter the book name: ")
        selection2 = input("Please enter the author name: ")
        selection3 = input("Please enter the release date: ")
        selection4 = input("Please enter the number of pages ")
        lib.addBook(selection1,selection2,selection3,selection4)

    elif selection == "3":
        book_name = input("Enter the name of the book you want to delete: ")    
        lib.removeBook(book_name)

    elif selection == "4":
        print("System is shutting down")  
        break

    else:
        print("You made an invalid choice. Please try again.")  