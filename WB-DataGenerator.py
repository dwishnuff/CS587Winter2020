'''
WB-DataGenerator is a simple script which generates benchmarking
data in the various Wisconsin Benchmark categories.

Programmed Jan 2020, by Danielle Beyer and William Mass
'''

import random as r
import csv

in_menu = True


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
    maxtuples = int(input("Please enter an integer value for maxtuples.  The Wisconsin Benchmark used 9999."))
    with open('benchmark_data.csv', 'w', newline='') as file:
        benchmark_writer = csv.writer(file)

        tuples_list = []
        for i in range(maxtuples):
            tuples_list.append(i)

        # copies the list of integers, then randomizes the copy
        rand_tuples_list = tuples_list.copy()
        r.shuffle(rand_tuples_list)
        unique1(rand_tuples_list, benchmark_writer)
        unique2(tuples_list, benchmark_writer)
        two(rand_tuples_list, benchmark_writer)
        four(rand_tuples_list, benchmark_writer)
        ten(rand_tuples_list, benchmark_writer)
        twenty(rand_tuples_list, benchmark_writer)
        one_percent(rand_tuples_list, benchmark_writer)
        ten_percent(rand_tuples_list, benchmark_writer)
        twenty_percent(rand_tuples_list, benchmark_writer)
        fifty_percent(rand_tuples_list, benchmark_writer)
        unique3(rand_tuples_list, benchmark_writer)


def unique1(rand_tuples_list, benchmark_writer):
    # unique1 - randomized tuples_list, 0 to (maxtuples - 1)
    benchmark_writer.writerow(rand_tuples_list)


def unique2(tuples_list, benchmark_writer):
    # unique2 - sequential tuples_list, 0 to (maxtuples - 1)
    benchmark_writer.writerow(tuples_list)


def two(rand_tuples_list, benchmark_writer):
    # two - 0 to 1 random (unique1 mod 2)
    two_list = []
    for i in rand_tuples_list:
        two_list.append(i % 2)
    benchmark_writer.writerow(two_list)


def four(rand_tuples_list, benchmark_writer):
    # four - 0 to 3 random (unique1 mod 4)
    four_list = []
    for i in rand_tuples_list:
        four_list.append(i % 4)
    benchmark_writer.writerow(four_list)


def ten(rand_tuples_list, benchmark_writer):
    # ten - 0 to 9 random (unique1 mod 10)
    ten_list = []
    for i in rand_tuples_list:
        ten_list.append(i % 10)
    benchmark_writer.writerow(ten_list)


def twenty(rand_tuples_list, benchmark_writer):
    # twenty - 0 to 19 random (unique1 mod 20)
    twenty_list = []
    for i in rand_tuples_list:
        twenty_list.append(i % 20)
    benchmark_writer.writerow(twenty_list)


def one_percent(rand_tuples_list, benchmark_writer):
    # onePercent - 0 - 99 random (unique1 mod 100)
    one_percent_list = []
    for i in rand_tuples_list:
        one_percent_list.append(i % 100)
    benchmark_writer.writerow(one_percent_list)


def ten_percent(rand_tuples_list, benchmark_writer):
    # tenPercent - 0 - 9 random (unique1 mod 10)
    ten_percent_list = []
    for i in rand_tuples_list:
        ten_percent_list.append(i % 10)
    benchmark_writer.writerow(ten_percent_list)


def twenty_percent(rand_tuples_list, benchmark_writer):
    # twentyPercent - 0 - 4 random (unique1 mod 5)
    twenty_percent_list = []
    for i in rand_tuples_list:
        twenty_percent_list.append(i % 5)
    benchmark_writer.writerow(twenty_percent_list)


def fifty_percent(rand_tuples_list, benchmark_writer):
    # fiftyPercent - 0 - 4 random (unique1 mod 2)
    fifty_percent_list = []
    for i in rand_tuples_list:
        fifty_percent_list.append(i % 2)
    benchmark_writer.writerow(fifty_percent_list)


def unique3(rand_tuples_list, benchmark_writer):
    # unique3 - 0 - (maxtuples - 1), described as (unique1)
    unique3_list = rand_tuples_list
    benchmark_writer.writerow(unique3_list)


def even_one_percent(rand_tuples_list, benchmark_writer):
    # evenOnePercent 0-198 random (onePercent * 2)
    even_one_percent_list = []
    for i in rand_tuples_list:
        even_one_percent_list.append((i % 100) * 2)
    benchmark_writer.writerow(even_one_percent_list)


def odd_one_percent(rand_tuples_list, benchmark_writer):
    #oddOnePercent 0-198 random (onePercent * 2)
    odd_one_percent_list = []
    for i in rand_tuples_list:
        odd_one_percent_list.append((i % 100) * 2) + 1
    benchmark_writer.writerow(odd_one_percent_list)

def stringu1(rand_tuples_list, benchmark_writer):
    for i in range(len(rand_tuples_list)):
        print("Foo")

def stringu2(benchmark_writer):
    print("Foo")

def string4(benchmark_writer):
    for i in range(len)


'''
stringu1 - random candidate key
stringu2 - random candidate key
string4 - cyclic
'''

def print_options():
    print("")
    print("The following options are available:")
    print("1) Generate all data.")
    print("0) Exit\n")

CLI(in_menu)