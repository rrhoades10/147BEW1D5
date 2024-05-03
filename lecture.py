# Errors and Exception Handling
# x = 1
# if x == 1
#     print("x is 1")
# gives a SyntaxError because we're missing a colon 

# NameError becuase name was never defined
# if name == "Lando":
#     print(True)

# ValueError - when we're working with an incorrect value
# we cant convert a string with alphabet characters into an integer
# number = int(input("Please enter a number: "))
# print(number)

# OverFlowError
# import math
# print(math.exp(1000)) #This number is too damn big!

# Mixing types that dont go together
# TypeError - we cannot add instances of a str to an int
# distance = 15+"300" 


# RunTimeError
# if something takes waaaay too long to complete
# def recursive_goof():    
#     recursive_goof()
# recursive_goof()

# try and except allows us to anticipate possible exception
# and gracefully log messages to the user or ourselves about how to fix

# try - attempt a block of code
# if that block runs succesfully then everything is cool
# if not it goes to the except block
# we can set the except block up to handle any exception or specific exceptions
# try:
#     user_input = int(input("Please enter a number"))
#     print(user_input)
# except: #anything that prevents our try from running will get caught in the except
#     print("Please enter a valid number!")

# # naming the exception to look out for
# try:
#     user_input = int(input("Please enter a number"))
#     print(user_input)
# except ValueError: #anything that prevents our try from running will get caught in the except
#     print("Please enter a valid number!")

# anticipating multiple errors
# try:
#     number = int(input("Enter a number"))
#     result = 100/number
#     print(result)
# except ValueError:
#     print("Please enter a valid number")

# except ZeroDivisionError:
#     # code to handle the exception
#     print("Sorry, infinity and beyond! is not a valid number right now..")

# creating exceptions for any number of errors
def perform_calculation(data):
    result = 0
    for item in data:
        result += item   
    average = result / len(data)
    return average
try: 
    # code that may cause an exception
    data = [1, "a", 2]
    calc_result = perform_calculation(data)
except (ValueError, ZeroDivisionError):
    # code here to handle the above exceptions
    print("Please provide a list of numbers and ensure that is not empty")
#  aliasing Exception as e
except Exception as e:
    print(f"An unknown error occurred: {e}")


# else in try and except is only going to run if there were no exceptions raised
# try: 
#     number = int(input("Enter a number "))
# except ValueError:
#     print("Thats not a number")
# else:
#     print("You entered a number succesfully")
#     print(number)

# finally - runs not matter what, whether we have a successful try or an exception is raised
# the finally shal run
# try: 
#     number = int(input("Enter a number "))
# except ValueError:
#     print("Thats not a number")
# finally:
#     print("This runs not matter what!")

# ============= Raising our own exceptions =====================
# fuel_level = 100
# if fuel_level < 0:
#     raise ValueError("Fuel Level cannot be negative")
# tank_capacity = 50   
# # creating your own exception
# class FuelTankOverflowError(Exception):
#     """Exception Raised when the fuel tank is overfilled"""
# if fuel_level > tank_capacity:
#     raise  FuelTankOverflowError("Fuel has exceeded the tank capacity")

# adding to a shopping cart with try and except
shopping_cart = []
bagged_items = []
# defining fuctions that will be called based on the user input in the driver code
# driver code is the while loop that continuously asks the user what theyd like to do
# takes in a cart parameter that holds the place of shopping_cart
# we CAN access shopping_cart within the function because its a global variable
# BUT we SHOULDNT access because its considered bad practice and icky code
# cart holds our place for shopping_cart which we use as an argument in the while loop below
def add_item(cart):
    item = input("What would you like to add to your cart? ").lower() #lowercases the string
    if item not in cart:
        cart.append(item)
    else:
        print(f"{item} is already in your cart!")

# cart holds our place for shopping_cart which we use as an argument in the while loop below
def remove_item(cart):
    item = input("Which item would you like to remove from your cart?").lower()
    # cart.remove(item)
    try:
        cart.remove(item)
    except ValueError:
        print(f"{item} is not in your cart, you can't remove something that doesn't exist!")

# cart holds our place for shopping_cart which we use as an argument in the while loop below
# bag holds the place of the bag list which we will use as an argument in the while loop below
def bag_item(cart, bag):
    # take an item from our cart, if it exists
    # and put it in our bag
    # remove our item from one list and add it to the other list
    # mark as "purchased"
    item = input("Which item would you like to bag?").lower()
    try:
        # remove from shopping_cart
        cart.remove(item)
        # adds to bag (at the end of the list)
        bag.append(item)
    except ValueError:
        print("That item is not in your cart...")

def view_items(cart, bag):
    response = input("Would you like to check your cart or your bag?").lower()
    if response == "cart":
        print("Here are your items!")
        for item in cart:
            print(item)
    elif response == "bag":
        print("Here are your purchased items: ")
        for item in bag:
            print(item)
    else:
        print("please enter a valid response!")             





# driver code that will call the functions based on the response variable thats holding the user input
# we're using cart and bag as parameters to be consistent with the above functions parameter naming conventions
# when we call the run function, we'll take shopping_cart and bagged_items as arguments
# cart and bag paramters will become the arguments in the functions within the run fuction
def run(cart,bag):
    while True:
        response = input("What would you like to do? add/remove/purchase/view/quit").lower()
        if response == "add":
            # using the shopping_cart list as an argumetn to fulfill the position of the cart parameter
            add_item(cart)
            print(cart)
        elif response == "remove":
            remove_item(cart)
            print(cart)

        elif response == "purchase":
            bag_item(cart, bag)
            print("Your purchased items: ")
            for item in bag:
                print(item)
        elif response == "view":
            view_items(cart, bag)

        elif response == "quit":
            for item in cart:
                print(item)
            for purchased_item in bag:
                print(purchased_item)
            break
        else:
            print("Please enter a valid response")


# calling the run function with shopping_cart and bagged_items arguments
run(shopping_cart, bagged_items)
