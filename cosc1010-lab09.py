# Luna Perez
# UWYO COSC 1010
# Submission Date 11/15/2024    
# Lab 09
# Lab Section: 13
# Sources, people worked with, help given to: TA ben wilkin, the join operator https://www.w3schools.com/python/ref_string_join.asp
# lecture 12 slides. 
# Comments
# Here

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.



             
        
# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be .
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.


# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.


# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""
class Pizza:
    '''A pizza order '''
    def __init__(self,size,sauce=''):
        '''initalize the order'''      
        self.sauce = self.pizza_sauce(sauce)
        self.topping = ['cheese']
        self.size = self.pizza_size(size)
        
        
    def pizza_size(self,size):
        '''Check the pizza size'''
        if not size.isnumeric() or int(size) <10: 
            print("our smallest is a 10 inch setting to small")
            self.size = 10
            return self.size
        
        
        else:
            self.size= int(size)
            return int(size)
    def get_size(self):
        '''size retreval command'''
        return self.size
    def add_toppings(self,topping):
        '''topping adding method'''
        if topping not in self.topping:
            self.topping.append(topping)
    def get_toppings(self):
        '''topping retreval method'''
        return self.topping
    def getammount(self):
        '''topping count retreval method'''
        return len(self.topping)
    def pizza_sauce(self,sauce):
         '''Check the sauce'''
         if sauce =="":
            return "red"
         return sauce


    

pizza_prompt = "Would you like to order a pizza   Exit to cancel: "



class Pizzaria:


    '''the ordering system'''
    def __init__(self):
        self.orders = 0
        self.price_per_top = 0.30
        self.price_per_inch = 0.60
        self.pizzas = []


    def place_order(self):
        '''order placment system'''
    
        while True:
            user_input= input(pizza_prompt)
            if user_input.lower() == 'exit':
                print (f'Total orders for the day #{self.orders}')
                break
            
            size = input("Please enter a size: ")
            sauce = input("Please enter your sauce\nleave blank for red: ")
            pizza = Pizza(size,sauce)
            while True:
                topping_inp = input("Please enter your topping\nleave blank to end: ")
                if topping_inp == "":
                    break
                
                pizza.add_toppings(topping_inp)
    
            
                
            self.pizzas.append(pizza)
            self.orders += 1
            self.Get_recipt()
            

    def getprice(self,pizza):
        '''Detertime the price of the pizza'''
 
        price_per_za=(pizza.get_size() * self.price_per_inch) + pizza.getammount() * self.price_per_top
        return price_per_za
    
    

    def Get_recipt(self):
        total_price = 0
        price = 0
        ''' print out a summary'''
        for pizza in self.pizzas:
            price = 0
            price = self.getprice(pizza)
            total_price += price
        print(f"\nYou got a pizza with:")
        print(f"Size {pizza.get_size()}")
        print(f'with {pizza.sauce} sauce')
        print(f"and with some {' ,'.join(pizza.get_toppings())}")
        print(f"toppings cost{(pizza.getammount())* self.price_per_top}")
        print(f"The total price is {total_price}")
        print(f"you are order number #{self.orders}")


Pj = Pizzaria()
Pj.place_order()