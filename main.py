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