#11/12/22, Arhanth Sarnikar
#This is a class for book objects which will be refrenced in another program

class Book:
    #Constructor
    def __init__(self, objTitle = "None", objAuthor = "Unknown", objGenre = "Unknown", objPrice = "Price"):
        self.title = objTitle
        self.author = objAuthor
        self.genre = objGenre
        self.price = objPrice

    #returns book information
    def __str__(self):
        return "Title: " + self.title + "\n" + "Author: " + self.author + "\n" + "Genre: " + self.genre + "\n" + "Price: " + self.price
        
    
        
