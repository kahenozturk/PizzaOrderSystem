from pizza import *
import csv
import datetime

def get_user_info():
    name = input("Enter your name: ")
    
    while True:
        id_number = input("Enter your ID number (11 digits): ")
        if len(id_number) != 11 or not id_number.isdigit():
            print("Invalid ID number. Please enter a valid 11-digit number.")
        else:
            break
    
    while True:
        cc_number = input("Enter your credit card number (16 digits): ")
        if len(cc_number) != 16 or not cc_number.isdigit():
            print("Invalid credit card number. Please enter a valid 16-digit number")
        else:
            break
    
    while True:
        cc_password = input("Enter your credit card password (4 digits): ")
        if len(cc_password) != 4 or not cc_password.isdigit():
            print("Invalid credit card password. Please enter a valid 4-digit number.")
        else:
            break
    
    return name, id_number, cc_number, cc_password

def main():
 # Read menu options from file
    menu_options = {}
    with open('Menu.txt', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=':')
        section = ''
        for row in reader:
            if row and row[0]:
                if row[0].startswith('*'):
                    section = row[0].strip('*').strip()
                    menu_options[section] = []
                else:
                    menu_options[section].append((row[0].strip(), row[1].strip()))


    # Print pizza options
    print("* Please Choose a Pizza Base:")
    for option in menu_options['Please Choose a Pizza Base']:
        print(option[0] + ': ' + option[1])

    # Get pizza choice from user
    while True:
        pizza_choice = input("Enter the number for your pizza choice: ")
        if pizza_choice in [option[0] for option in menu_options['Please Choose a Pizza Base']]:
            break
        print("Invalid choice. Please try again.")
    pizza = None
    for option in menu_options['Please Choose a Pizza Base']:
        if pizza_choice == option[0]:
            pizza_class = globals()[option[1]]
            pizza = pizza_class()
            break

    print("\nYou have selected the " + pizza.get_description())

    # Print sauce options
    print("* and sauce of your choice:")
    for option in menu_options['and sauce of your choice']:
        print(option[0] + ': ' + option[1])

    # Get sauce choices from user
    toppings = []
    while True:
        sauce_choice = input("Enter the number for your sauce choice (or '0' to finish): ")
        if sauce_choice == '0':
            break
        elif sauce_choice in [option[0] for option in menu_options['and sauce of your choice']]:
            toppings.append(sauce_choice)
        else:
            print("Invalid choice. Please try again.")

    # Apply sauce choices to pizza
    if toppings:
        sauce = None
        for topping in toppings:
            for option in menu_options['and sauce of your choice']:
                if topping == option[0]:
                    sauce_class = globals()[option[1]]
                    sauce = sauce_class(sauce) if sauce else sauce_class(pizza)
                    break
            else:
                print("Invalid choice. Please try again.")
        print("\nYou have selected the following toppings: ", sauce.get_description())
    else:
        sauce = Plain(pizza)
        print("\nNo toppings selected. Your pizza will have plain sauce.")

    # Print total cost
    print("\nYour total cost is: ${:.2f}".format(sauce.get_cost()))


    # Process payment
        # Get user information
    name, id_number, cc_number, cc_password = get_user_info()
    
    # Print the order confirmation
    print("Thank you for your order, {}!".format(name))
    print("Your order {} has been placed.".format(sauce.get_description()))
    print("The total cost is ${}.".format(sauce.get_cost()))

    fields = ['Name', 'ID Number', 'Credit Card Number', 'Credit Card Password', 'Order Time', 'Pizza Description', 'Sauce Description', 'Total Cost']

    with open('Orders_Database.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(fields)

        writer.writerow([name, id_number, cc_number, cc_password, datetime.datetime.now(), pizza.get_description(), sauce.get_description(), sauce.get_cost()])


if __name__ == "__main__":
    main()