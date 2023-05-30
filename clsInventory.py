#11/12/22, Arhanth Sarnikar
#This is a class for inventory objects which will be refrenced in another program

#Importing Book Objects
from clsBook import Book


class Inventory:
    #Class variable
    books = {}

    
    #Constructor
    def __init__(self):
        self.books = {}
        
    #AddBooks to inventory
    def addBooks(self):
        #Opens .txt file
        bookfile = open("booklist.txt", "r")
        #Transfers information into list with .readlines()
        booklist = bookfile.readlines()
        #close
        bookfile.close()
        #For loop adds items to map
        for i in range(0, len(booklist)):
            #Splits items 
            bookitems = booklist[i].split(",")
            #Adding book information to variables
            item_num = bookitems[0]
            book_title = bookitems[1]
            book_author = bookitems[2]
            book_genre = bookitems[3]
            book_price = bookitems[4]

            #adding book information to book object
            book1 = Book(book_title, book_author, book_genre, book_price)
            
            #adding to map
            self.books[item_num] = book1

    #Function displays all books available using for loop        
    def display(self):
        for a, b in self.books.items():
            print("")
            print("========================")
            print("Item Number " + a)
            print(b)
            print("========================")
            
            
#Subclass Cart
class Cart(Inventory):

    def addBooks(self):
        print("")

    
    #AddBooks Function adds books based to map based on user input
    def addBooks(self, item_num, book1):
        self.books[item_num] = book1

    #Checkout displays total price
    def checkout(self):
        print("Your total price is: ")
        total = 0
        for a, b in self.books.items():
            #Total is converted to float then rounded
            total = float(b.price.rstrip("\n")) + total
            t = round(total, 2)

        #Printing Total
        print(str(t))
        print("")
        print("Thank you for your business!")
            
            
            
            
       


    

    

