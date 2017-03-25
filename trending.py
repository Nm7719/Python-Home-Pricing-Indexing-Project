"""
File: trending.py
Assignment: Computes the top and bottom trending regions based on
            their growth between a given starting and a given ending point.
Author: Noor Mohammad, nm7719@rit.edu
Date: November 29 2016
"""

from indexTools import *

def cagr(idxlist, periods):
    """
    :pre-condition: HPI0 is the index value of the earlier period.
    :param idxlist: A 2-item list of [HPI0, HPI1]
    :param periods: The number(N) of periods (years) between two HPI values.
    :return: A float representing the compound annual growth rate, CAGR, of the
             index values in the list for the specified period.
    """
    return (((idxlist[1]/idxlist[0]) ** (1/periods)) - 1) * 100

def calculate_trends(data,year0,year1):
    """
    :pre-conditions: Year0 must be less than year1
    :param data: A dictionary from region to a list of AnnualHPI.
    :param year0: Specifies the starting year of interest
    :param year1: Specifies the ending year of interest.
    :return: A list of (region, rate) tuples sorted in descending order
             by the compound annual growth rate. The rate is the compound
             annual, year-to-year rate of change between year0 and year1 values.
    :post-conditions: Ignores the region that lacks an entry for either year.
    """
    if year0 > year1:
        raise Exception
    period = year1 - year0
    ad = []
    for i in data.keys():
        length = len(data[i])
        for x in range(len(data[i])):
            if data[i][x].year == year0:
                length = len(data[i]) - length
                while length < len(data[i]):
                    if data[i][length].year == year1:
                        ad.append((i,[data[i][x].index,data[i][length].index]))
                        length = len(data[i])
                        x = len(data[i])
                    length+=1

    lst = []
    for i in ad:
        lst.append((i[0],cagr(i[1],period)))

    sort_lst = sorted(lst, key=lambda x: x[1], reverse=True)

    return sort_lst

def main():
    """
     Prompts the user for an input data file, a starting year, and an ending year.
     Prints the top 10 growth and bottom 10 growth regions in that timespan.
    :return:
    """
    filename = input("Enter house price index file: ")
    filename = "data/" + filename
    year0 = int(input("Enter start year of interest: "))
    year1 = int(input("Enter ending year of interest: "))
    x = 1

    if "ZIP" in filename or "zip" in filename:
        data = read_zip_house_price_data(filename)
    else:
        data = read_state_house_price_data(filename)
        data = annualize(data)


    lst = calculate_trends(data,year0,year1)
    print("")
    print(str(year0) + "-" + str(year1) + " Compound Annual Growth Rate\nThe Top 10:")
    for i in lst[:10]:
        print(x,":",i)
        x += 1
    x = len(lst) - 9
    print("The Bottom 10:")
    for i in lst[-10:]:
        print(x,":",i)
        x += 1
if __name__ == '__main__':
    # main runs only when directly invoking this module
    main()