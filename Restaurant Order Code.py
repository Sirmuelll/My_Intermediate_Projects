"""This is a script that accepts customers orders and also estimate the time that their order would arrive
"""
# create a general welcome message
# create a function that lists the available food
# create a function that accepts the user choice and also ask if the user would like to re-order
# if yes, the food menu should pop-up again
# if no, there should be a thank you message, the list of food bought, the total cost, and the estimated time of delivery

# import the needed modules
import random
import time
import pyinputplus as pyip

# Here is a message that welcomes the customer
welcome = "Hello, Welcome to forks and Fingers\n"
for x in welcome:
    print(x, end='', flush=True)
    time.sleep(0.1)

# This is the counter that adds up the prices of everything
a = 0


# This generates a code for the customer's order


def code_generator():
    code_character = 'abcdefghijklmnopqrstuvwxyz1234567890'
    generate_code = ''
    for code in range(8):
        generate_code += random.choice(code_character)
    print(f"Your order number is {generate_code}")


# This is the code that asks customer if they wish to order more


def response():
    while True:
        user_response = pyip.inputYesNo(
            "Would you like to order more?").lower()
        if user_response == "yes":
            order_food()
        else:
            print("Thanks for ordering")
        break


def reorder_and_multiplier(x, meal_name):
    # After the customer chooses a meal, this line of code splits the meal name from its price so that the next line of code would be properly executed

    meal_namee = meal_name.split('-')[0]
    how_many = pyip.inputInt(
        f"You have ordered {meal_namee}, but how many pieces of it would you like?")  # This line asks the buyer how many piece of that meal he/she wishes to order
    # This line multiplies the price of the meal by the quantity ordered
    current_pricee = x * how_many
    return current_pricee


def order_food():
    global a

    # This creates the list of the available meal or snacks

    menu_list = pyip.inputMenu(
        ["Croissant - $18", "Flat Bread - $40", "Sausage - $25", "Bacon - $50", "Forest Ham - $15"], numbered=True, prompt="Here is our menu list:\n")

    if menu_list == "Croissant - $18":
        own_price = 18
        current_price = reorder_and_multiplier(own_price, menu_list)
        a += current_price
        response()
    elif menu_list == "Flat Bread - $40":
        own_price = 40
        current_price = reorder_and_multiplier(own_price, menu_list)
        a += current_price
        response()
    elif menu_list == "Sausage - $25":
        own_price = 25
        current_price = reorder_and_multiplier(own_price, menu_list)
        a += current_price
        response()
    elif menu_list == "Bacon - $50":
        own_price = 50
        current_price = reorder_and_multiplier(own_price, menu_list)
        a += current_price
        response()
    else:
        own_price = 15
        current_price = reorder_and_multiplier(own_price, menu_list)
        a += current_price
        response()


order_food()

code_generator()
print(f"Your total order costs ${a}")
