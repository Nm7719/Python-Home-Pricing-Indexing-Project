"""
File: timelinePlot.py
Assignment: Graph changes in HPI values over time.
            Two kind of graphs will be created:
                    A set of line graphs with one line for each region.
                    A set of 'box and whiskers' diagrams for one or more region.
Author: Noor Mohammad, nm7719@rit.edu
Date: November 29 2016
"""

from indexTools import *
import numpy.ma as ma
import numpy
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import copy

def build_plottable_array(xyears, regiondata):
    """
    :param xyears: A list of integer year values.
    :param regiondata: A list of AnnualHPI.
    :return: An array suitable for plotting with the matplotlib module.
    :post-conditions: Bridge the unavailable data gap.
    """
    lst = []
    for j in xyears:
        temp = False
        for i in regiondata:
            if j == i.year:
                temp = True
                lst.append(i.index)
        if not temp:
            lst.append(0)

    y = ma.array(lst)

    i = 0
    while i < len(lst):
        if lst[i] == 0:
            y[i] = ma.masked
        i += 1
    return y

def build_plottable_whisker_array(xyears, regiondata):
    """
    :param xyears: A list of integer year values.
    :param regiondata: A list of AnnualHPI.
    :return: An array of indexes for plotting with the matplotlib module.
    """
    lst = []
    for j in xyears:
        temp = False
        for i in regiondata:
                lst.append(i.index)
    y = ma.array(lst)
    return y

def filter_years(data,year0,year1):
    """
    :param data: A dictionary mapping regions to lists of AnnualHPI objects.
                 such that AnnualHPI is within [year0 ... year1].
    :param year0: Specifies the starting year of interest.
    :param year1: Specifies the ending year of interest.
    :return: A dictionary mapping regions to lists of HPI values that are
             within the year0 to year1 inclusive range.
    :pre-conditions: Year0 must be less than or equal to Year1.
    """
    if year0 > year1:
        raise Exception
    lst = [i for i in range(year0,year1+1)]
    sub = {}
    for i in data.keys():
        sub[i] = []
        for val in data[i]:
            if val.year in lst:
                sub[i].append(val)
    return sub

def plot_HPI(data,regionList):
    """
    :param data: A dictionary mapping a state or zip code to a list of AnnualHPI.
    :param regionList: A list of key values whose type isstring.
    :return: NoneType. Plots a timeline from point to point over the time period.
    """
    lst = []
    minimum = 2016
    maximum = 0
    for i in range(len(regionList)):
        for x in data[regionList[i]]:
            if x.year < minimum:
                minimum = x.year
            if x.year > maximum:
                maximum = x.year
    temp = [i for i in range(minimum,maximum+1)]

    for i in regionList:
        lst.append(build_plottable_array(temp,data[i]))
    mc = ma.array(temp)
    plt.figure()
    for i in range(len(regionList)):
        plt.plot(mc,lst[i],c=numpy.random.rand(3,1),marker='*',label=regionList[i])
    plt.title('Home Price Indices: '+str(temp[0])+'-'+str(temp[len(temp)-1]))
    plt.legend(loc='upper left')
    plt.show()

def plot_whiskers(data,regionList):
    """
    :param data: A dictionary mapping a state or zip code to a list of AnnualHPI.
    :param regionList: A list of key values whose type isstring.
    :return: Plots a whisker plot of the given regions.
    """
    lst = []
    minimum = 2016
    maximum = 0
    for i in range(len(regionList)):
        for x in data[regionList[i]]:
            if x.year < minimum:
                minimum = x.year
            if x.year > maximum:
                maximum = x.year
    temp = [i for i in range(minimum, maximum + 1)]

    for i in regionList:
        lst.append(build_plottable_whisker_array(temp,data[i]))

    meanpointprops = dict(marker='D')
    plt.figure()
    plt.boxplot(lst,labels=regionList,meanprops=meanpointprops,showmeans = True,)
    plt.title('Home Price Index Comparison. Median is a line. Mean is a diamond.')
    plt.show()

def main():
    """
    Prompts the user for an input data file, a starting year, an ending year,
    and finally a list of regions for which to produce plots.
    :return: NoneType.
    """
    filename = input("Enter house price index filename: ")
    filename = "data/" + filename
    year0 = int(input("Enter the start year of the range to plot: "))
    year1 = int(input("Enter the end year of the range to plot: "))

    lst = []
    while True:
        region = input("Enter next region for plots(<ENTER> to stop): ")
        if region == "":
            break
        else:
            lst.append(region)

    if "ZIP" in filename or "zip" in filename:
        data = read_zip_house_price_data(filename)
        subset = filter_years(data, year0, year1)
    else:
        data = read_state_house_price_data(filename)
        for i in lst:
            print_range(data,i)
        annual = annualize(data)
        subset = filter_years(annual,year0,year1)
    print("Close display window to continue")
    plot_HPI(subset, lst)
    print("Close display window to continue")
    plot_whiskers(subset, lst)

if __name__ == '__main__':
    # main runs only when directly invoking this module
    main()
