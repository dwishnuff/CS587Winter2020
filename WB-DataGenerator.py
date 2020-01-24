'''
WB-DataGenerator is a simple script which generates benchmarking
data in the various Wisconsin Benchmark categories.

Programmed Jan 2020, by Danielle Beyer and William Mass
'''

import random as r
import csv

in_menu = True

def print_options():
    print("")
    print("The following options are available:")
    print("1) Generate all data.")
    print("0) Exit\n")


def CLI(in_menu):
    while in_menu == True:
        print("Wisconsin Benchmark Data Generator will produce data for Wisconsin Benchmark categories.\n")
        print_options()
        while True:
            try:
                selection = int(input("Please make a selection:"))
                break
            except:
                print("That's not a valid option! Please stop typing in nonsense.")
                print_options()
                continue
        if selection == 0:
            in_menu = False
        elif selection == 1:
            benchmarking_scriptwriter()
        else:
            print("That's not a valid option! Please select an option from the menu.")
    print("Exiting program! Thanks for using Wisconsin Benchmark Data Generator!")


def benchmarking_scriptwriter():
        print("Obviously, we make this do something")


CLI(in_menu)