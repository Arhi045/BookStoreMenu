#11/12/22, Arhanth Sarnikar
#The purpose of this program is to integrate and use three different classes from different files
#These classes will be used to create a menu for a company that sells books
#There will be different options the user can choose based on a main menu

#Importing Classes
from clsInventory import Inventory, Cart
#Creating objects
inv = Inventory()
inv.addBooks()

cart = Cart()

#Function to display Menu
def menu():
    print("")
    print("Welcome to the ABC Book Store!")
    print("------------------------------")
    print("1: Display Books")
    print("2: Add to Cart")
    print("3: Show Cart")
    print("4: Checkout")
    print("5: Quit")
    #Collects user's input
    option = int(input("Select an Option: "))
    print("")
    
    #return
    return option

#Main Program
selection = 0
#While loop keeps running until user elects
while selection != 5:
    #Displays menu and gathers input using menu function
    selection = menu()
    if selection == 1:
        #Displays based on inventory function
        inv.display()
    elif selection == 2:
        #Checks for item number
        item_num = input("Please enter the item number of the book you want to add to the cart: ").rstrip("\n")
        cart.addBooks(item_num, inv.books[item_num])
    elif selection == 3:
        #Displays current cart
        cart.display()
    elif selection == 4:
        #Checkout function displays total value
        cart.checkout()
    else:
        print("")
        print("Thank you for shopping at the ABC Book Store! ")



