'''
WB-DataGenerator is a simple script which generates benchmarking
data in the various Wisconsin Benchmark categories.

Programmed Jan 2020, by Danielle Beyer and William Mass
'''

import csv
import random as r
import time


def CLI(in_menu):
    while in_menu == True:
        print(
            "Wisconsin Benchmark Data Generator will produce data for Wisconsin Benchmark categories.\n"
        )
        print_options()
        while True:
            try:
                selection = int(input("Please make a selection:"))
                break
            except:
                print(
                    "That's not a valid option! Please stop typing in nonsense."
                )
                print_options()
                continue
        if selection == 0:
            in_menu = False
        elif selection == 1:
            listwriter()
            print("CSV created.")
        else:
            print(
                "That's not a valid option! Please select an option from the menu."
            )
    print(
        "Exiting program! Thanks for using Wisconsin Benchmark Data Generator!"
    )


def listwriter():
    maxtuples = int(
        input(
            "Please enter an integer value for maxtuples. The Wisconsin Benchmark used 9999."
        ))
    start_time = time.time()
    tuples_list = []
    for i in range(maxtuples):
        tuples_list.append(i)
    rand_tuples_list = tuples_list.copy()
    r.shuffle(rand_tuples_list)
    unique1_list = rand_tuples_list.copy()
    unique2_list = unique2(tuples_list)
    two_list = two(unique1_list)
    four_list = four(unique1_list)
    ten_list = ten(unique1_list)
    twenty_list = twenty(unique1_list)
    one_percent_list = one_percent(unique1_list)
    ten_percent_list = ten_percent(unique1_list)
    twenty_percent_list = twenty_percent(unique1_list)
    fifty_percent_list = fifty_percent(unique1_list)
    unique3_list = unique3(unique1_list)
    even_one_percent_list = even_one_percent(unique1_list)
    odd_one_percent_list = odd_one_percent(unique1_list)
    stringu1_list = []
    stringu2_list = []
    j = 0
    while j < len(tuples_list):
        stringu1_list.append(stringu1(unique1_list[j]))
        stringu2_list.append(stringu1(unique2_list[j]))
        j += 1
    stringu4_list = string4(maxtuples)

    with open('benchmark_data.csv', 'w', newline='') as file:
        benchmark_writer = csv.writer(file)
        for i in range(maxtuples):
            benchmark_writer.writerow([
                unique1_list[i], unique2_list[i], two_list[i], four_list[i],
                ten_list[i], twenty_list[i], one_percent_list[i],
                ten_percent_list[i], twenty_percent_list[i],
                fifty_percent_list[i], unique3_list[i],
                even_one_percent_list[i], odd_one_percent_list[i],
                stringu1_list[i], stringu2_list[i], stringu4_list[i]
            ])
    end_time = time.time()
    print("Data generated in %f seconds!" % (end_time - start_time))


def unique1(tuples_list):
    # unique1 - randomized tuples_list, 0 to (maxtuples - 1)
    rand_tuples_list = tuples_list.copy()
    # unique_1 = r.shuffle(rand_tuples_list)
    return r.shuffle(rand_tuples_list)  # returns entire list


def unique2(tuples_list):
    # unique2 - sequential tuples_list, 0 to (maxtuples - 1)
    copied_list = tuples_list.copy()
    return copied_list


def two(rand_tuples_list):
    # two - 0 to 1 random (unique1 mod 2)
    two_list = []
    for i in rand_tuples_list:
        two_list.append(i % 2)
    return two_list


def four(rand_tuples_list):
    # four - 0 to 3 random (unique1 mod 4)
    four_list = []
    for i in rand_tuples_list:
        four_list.append(i % 4)
    return four_list


def ten(rand_tuples_list):
    # ten - 0 to 9 random (unique1 mod 10)
    ten_list = []
    for i in rand_tuples_list:
        ten_list.append(i % 10)
    return ten_list


def twenty(rand_tuples_list):
    # twenty - 0 to 19 random (unique1 mod 20)
    twenty_list = []
    for i in rand_tuples_list:
        twenty_list.append(i % 20)
    return twenty_list


def one_percent(rand_tuples_list):
    # onePercent - 0 - 99 random (unique1 mod 100)
    one_percent_list = []
    for i in rand_tuples_list:
        one_percent_list.append(i % 100)
    return one_percent_list


def ten_percent(rand_tuples_list):
    # tenPercent - 0 - 9 random (unique1 mod 10)
    ten_percent_list = []
    for i in rand_tuples_list:
        ten_percent_list.append(i % 10)
    return ten_percent_list


def twenty_percent(rand_tuples_list):
    # twentyPercent - 0 - 4 random (unique1 mod 5)
    twenty_percent_list = []
    for i in rand_tuples_list:
        twenty_percent_list.append(i % 5)
    return twenty_percent_list


def fifty_percent(rand_tuples_list):
    # fiftyPercent - 0 - 4 random (unique1 mod 2)
    fifty_percent_list = []
    for i in rand_tuples_list:
        fifty_percent_list.append(i % 2)
    return fifty_percent_list


def unique3(rand_tuples_list):
    # unique3 - 0 - (maxtuples - 1), described as (unique1)
    unique3_list = rand_tuples_list.copy()
    return unique3_list


def even_one_percent(rand_tuples_list):
    # evenOnePercent 0-198 random (onePercent * 2)
    even_one_percent_list = []
    for i in rand_tuples_list:
        even_one_percent_list.append((i % 100) * 2)
    return even_one_percent_list


def odd_one_percent(rand_tuples_list):
    # oddOnePercent 0-198 random (onePercent * 2)
    odd_one_percent_list = []
    for i in rand_tuples_list:
        odd_one_percent_list.append(((i % 100) * 2) + 1)
    return odd_one_percent_list


def stringu1(rand_tuples_list):
    temp = []
    workingnumber = rand_tuples_list

    while workingnumber > 0:
        convertednumber = (workingnumber % 26) + ord('A')
        temp.append(chr(convertednumber))
        workingnumber = int(workingnumber / 26)

    j = 7 - len(temp)
    reversedtemp = temp[::-1]
    stringify = ''
    for element in reversedtemp:
        stringify += element
    result = (stringify + ('A' * j) + ('x' * 45))

    return result


def string4(maxtuples):
    string4_list = []
    for i in range(maxtuples):
        if i % 4 == 0:
            string4_list.append("AAAA" + ('x' * 48))
        if i % 4 == 1:
            string4_list.append("HHHH" + ('x' * 48))
        if i % 4 == 2:
            string4_list.append("OOOO" + ('x' * 48))
        if i % 4 == 3:
            string4_list.append("VVVV" + ('x' * 48))
    return string4_list


def print_options():
    print("")
    print("The following options are available:")
    print("1) Generate all data.")
    print("0) Exit\n")


in_menu = True
CLI(in_menu)
