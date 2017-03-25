"""
File: periodRanking.py
Assignment: A program which can compute the rankings of states or zip codes
            for a given year, or for a given quarter
Author: Noor Mohammad, nm7719@rit.edu
Date: November 29 2016
"""

from indexTools import *

def quarter_data(data,year,qtr):
    """
    :pre-condition: data must be a dictionaries whose value type is QuarterHPI.
    :param data: The data is a dictionary mapping a state region
                 to a list of Quarter HPI instances.
    :param year: The year of interest
    :param qtr:  The quarter of interest, between 1 and 4.
    :return: A list of (region, HPI) tuples sorted from high to low value HPI.
    """
    qd = []
    for i in data.keys():
        for x in data[i]:
            if x.year == year and x.qtr == qtr:
                qd.append((i,x.index))

    sort_qd = sorted(qd, key=lambda x: x[1], reverse=True)

    return sort_qd

def annual_data(data,year):
    """
    :pre-condition: data must be a dictionaries whose value type is AnnualHPI.
    :param data: The data is a dictionary mapping a state or zip code
                 to a list of AnnualHPI objects.
    :param year: The year of interest.
    :return: A list of (region, HPI) tuples sorted from high to low value HPI.
    """
    ad = []
    for i in data.keys():
        for x in data[i]:
            if x.year == year:
                ad.append((i,x.index))

    sort_ad = sorted(ad, key=lambda x: x[1], reverse=True)
    for i in data:
        print(i)
    return sort_ad

def main():
    """
    Prompts the user for an input data file and a year of interest
    and determine which file processing function to use.
    Thereafter print the top 10 and bottom 10 annual ranking of the year.
    :return: NoneType
    """
    filename = input("Enter region-based house price index filename: ")
    filename = "data/" + filename
    year = int(input("Enter year of interest for house prices: "))

    if "ZIP" in filename or "zip" in filename:
        data = read_zip_house_price_data(filename)
        ad = annual_data(data,year)
    else:
        data = read_state_house_price_data(filename)
        qd = annualize(data)
        ad = annual_data(qd, year)

    print("")
    print_ranking(ad, str(year) + " Annual Ranking")

if __name__ == '__main__':
    # main runs only when directly invoking this module
    main()