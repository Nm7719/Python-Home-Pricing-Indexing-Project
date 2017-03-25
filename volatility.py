"""
File: volatility.py
Assignment: Annualize all quarterly datasets.
Author: Noor Mohammad, nm7719@rit.edu
Date: November 29 2016
"""

from indexTools import *
from math import *

def average(nums):
    """
    :param nums: A list of float values to average together.
    :return: A float representing the average value of the given numeric dataset.
    """
    total = 0
    for i in nums:
        total += i
    return (total / len(nums))

def deviation_squared(nums, avg):
    """
    :param nums: A list of numeric values
    :param avg: The average of the list of numeric values.
    :return: An array of float values representing the square of the deviations
             of the data from the data average.
    """
    lst = []
    for i in nums:
        deviation = (i - avg) ** 2
        lst.append(deviation)
    return lst

def measure_volatility(data):
    """
    :param data: A dictionary from region to list of AnnualHPI values.
    :return: A list of (region, standard_deviation) tuples sorted from
             high to low values.
    """
    lst = []
    for i in data.keys():
        temp = []
        for x in data[i]:
            temp.append(x.index)
        avg = deviation_squared(temp,average(temp))
        tot_avg = 0
        for x in avg:
            tot_avg += x
        tot_avg = sqrt(tot_avg / len(avg))
        lst.append((i,tot_avg))


    sort_lst = sorted(lst, key=lambda x: x[1], reverse=True)

    return sort_lst

def main():
    """
    Prompts for the home price data file and the state or zip region of interest
    Prints a table of the top/bottom 10 regions sorted by their measured volatility.
    :return:
    """
    filename = input("Enter region-based house price index filename: ")
    filename = "data/" + filename
    region = input("Enter the region of interest: ")

    if "ZIP" in filename or "zip" in filename:
        data = read_zip_house_price_data(filename)
    else:
        data = read_state_house_price_data(filename)
        data = annualize(data)

    lst = measure_volatility(data)
    x = 1
    print("Annualized Price Standard Deviation, High to Low\nThe Top 10:")
    for i in lst[:10]:
        print(x,":",i)
        x += 1
    x = len(lst) - 9
    print("The Bottom 10:")
    for i in lst[-10:]:
        print(x,":",i)
        x += 1
    print("\nNote: Absence of data can increase the apparent variation.")
    for i in range(len(lst)):
        if lst[i][0] == region:
            print("Standard deviation for",region,"is",lst[i][1])

if __name__ == '__main__':
    # main runs only when directly invoking this module
    main()
