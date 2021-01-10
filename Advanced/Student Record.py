# This program maintains student records
from random import randint
import sys

dt = {}

def main_menu():
    option = input(
        "To add a student record, type 'a'\nTo search for a record, type 's'\nTo print all records, type 'p'\nTo quit, type 'q'\nEnter your option: ")
    if option.lower() == 'a':
        add_record()
    elif option.lower() == 's':
        search_record()
    elif option.lower() == 'p':
        print_record()
    elif option.lower() == 'q':
        print("Thank you for using our system. Goodbye!")
        sys.exit()
    else:
        print("Sorry. You entered a letter that is not an option. Please try again.")
        main_menu()

def add_record():
    fname = input("Enter the first name: ")
    lname = input("Enter the last name: ")
    grade = int(input("Enter the grade: "))
    room = int(input("Enter the room number: "))
    r_d = {}
    r_d["First Name"] = fname
    r_d["Last Name"] = lname
    r_d["Grade"] = grade
    r_d["Room #"] = room
    i_d = randint(1, 100)
    dt[i_d] = r_d
    print(dt)
    main_menu()

main_menu()