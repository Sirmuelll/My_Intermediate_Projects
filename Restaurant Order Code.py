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
    time.sleep(0.09)

# This is the counter that adds up the prices of everything
all_price = 0


# This generates a code for the customer's order


def code_generator():
    code_character = 'abcdefghijklmnopqrstuvwxyz1234567890'
    generate_code = ''
    for code in range(6):
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


# After a user must have selected a menu fron the list, this block asks how many pieces/plates of the menu they would like to order and returns the current price by multiplying the price of that menu with the number of unit ordered
def reorder_and_multiplier(x, meal_name):
    # After the customer chooses a meal, this line of code splits the meal name from its price so that the next line of code would be properly executed

    meal_namee = meal_name.split('-')[0]
    how_many = pyip.inputInt(
        f"You have ordered {meal_namee}, but how many pieces of it would you like?")  # This line asks the buyer how many piece of that meal he/she wishes to order
    # This line multiplies the price of the meal by the quantity ordered
    current_pricee = x * how_many
    return current_pricee


# This block of code adds the current_pricee from the above code to the general total cost "a".
def total(own_price, menu_list):
    global all_price
    current_price = reorder_and_multiplier(own_price, menu_list)
    all_price += current_price
    response()


# This is the main food order block
def order_food():
    # This creates the list of the available meal or snacks

    menu_list = pyip.inputMenu(
        ["Croissant - $18", "Flat Bread - $40", "Sausage - $25", "Bacon - $50", "Forest Ham - $15"], numbered=True,
        prompt="Here is our menu list:\n")

    if menu_list == "Croissant - $18":
        own_price = 18
        total(own_price, menu_list)

    elif menu_list == "Flat Bread - $40":
        own_price = 40
        total(own_price, menu_list)

    elif menu_list == "Sausage - $25":
        own_price = 25
        total(own_price, menu_list)

    elif menu_list == "Bacon - $50":
        own_price = 50
        total(own_price, menu_list)

    else:
        own_price = 15
        total(own_price, menu_list)


def main():
    order_food()
    code_generator()
    print(f"Your total order costs ${all_price}")


if __name__ == "__main__":
    main()
