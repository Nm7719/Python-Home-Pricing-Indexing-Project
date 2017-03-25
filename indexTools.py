"""
File: indexTools.py

Assignment: Contains a set of utilities which includes
            and functions used by the other program tasks.
            These are used to open files and create either
            a Quarter or an Annual Home Price Index for either
            a zip file or a state file.
Author: Noor Mohammad, nm7719@rit.edu

Date: November 29 2016
"""
from rit_lib import *

class QuarterHPI(struct):
    """
    Class with three slots to record the year, quarter
    and index of a state or a zip.
    """
    _slots = ((int,"year"),(int,"qtr"),(float,"index"))

class AnnualHPI(struct):
    """
    Class with two slots to record the year and index of a zip code.
    """
    _slots = ((int,"year"),(float,"index"))

def read_state_house_price_data(filepath):
    """
    Takes in a state file path and uses it to create a dictionary of
    all states to record the available year, quarter, and index.
    :pre-condition: File path must exist, and must be a state file.
    :param filepath: A string, giving the path name of a data file.
    :return: A dictionary mapping state abbreviations to lists of QuarterHPI
             objects.
    """
    file = open(filepath)
    state_data = {}
    for line in file:
        line = line.split()
        if len(line[0]) != 2:
            pass
        elif line[3] == ".":
            print("data unavailable:")
            for i in line:
                print(i,end=" ")
            print("\n")
        else:
            if line[0] in state_data:
                year = int(line[1])
                qtr = int(line[2])
                index = float(line[3])
                state_data[line[0]].append(QuarterHPI(year,qtr,index))
            else:
                year = int(line[1])
                qtr = int(line[2])
                index = float(line[3])
                state_data[line[0]] = [QuarterHPI(year,qtr,index)]
    return state_data

def read_zip_house_price_data(filepath):
    """
    Takes in a zip code file path and uses it to create a dictionary of
    all states to record the available year, quarter, and index.
    :pre-condition: File path must exist, and must be a zip file.
    :param filepath: A string, giving the path name of a data file.
    :return: A dictionary mapping zip codes to lists of AnnualHPI objects.
    """
    file = open(filepath)
    zip_data = {}
    count = 0
    uncounted = 0
    for line in file:
        line = line.split()
        if not line[0].isdigit():
            pass
        elif line[3] == ".":
            uncounted += 1
        else:
            count += 1
            if line[0] in zip_data:
                year = int(line[1])
                index = float(line[3])
                zip_data[line[0]].append(AnnualHPI(year, index))
            else:
                year = int(line[1])
                index = float(line[3])
                zip_data[line[0]] = [AnnualHPI(year, index)]

    print("count:",count,"uncounted:",uncounted)
    return zip_data

def index_range(data,region):
    """
    Given a dictionary and a region name, identify the lowest index,
    and the largest index within that region and return the tuple of it.
    :param data: A dictionary mapping regions to lists of HPI objects.
    :param region: A region name
    :return: A tuple of the minimum and maximum index values of the HPI objects
    """
    min = data[region][0].index
    min_index = 0
    max = data[region][0].index
    max_index = 0
    for i in range(1,len(data[region])):
        if data[region][i].index > max:
            max = data[region][i].index
            max_index = i
        if data[region][i].index < min:
            min = data[region][i].index
            min_index = i

    return(data[region][min_index],data[region][max_index])

def print_range(data,region):
    """
    Finds the highest index and lowest index for a given region.
    :param data: A dictionary mapping regions to lists of HPI objects.
    :param region: A region name
    :return: NoneType, prints the lowest and highest values of a specified HPI.
    """
    print("Region:",region)
    min = data[region][0].index
    min_index = 0
    max = data[region][0].index
    max_index = 0
    for i in range(1, len(data[region])):
        if data[region][i].index > max:
            max = data[region][i].index
            max_index = i
        if data[region][i].index < min:
            min = data[region][i].index
            min_index = i
    if isinstance(data[region][0],QuarterHPI):
        print("Low: year/quarter/index:", data[region][min_index].year, "/", data[region][min_index].qtr, "/", min)
        print("High: year/quarter/index:", data[region][max_index].year, "/", data[region][max_index].qtr, "/", max)
    else:
        print("Low: year/index:", data[region][min_index].year, "/", min)
        print("High: year/index:", data[region][max_index].year, "/", max)


def print_ranking(data,heading="Ranking"):
    """
    Given a sorted list, prints the top ten and bottom ten values of the list.
    :param data: A sorted list of objects
    :param heading: A text message whose default value is "Ranking"
    :return: NoneType, prints a table of processed data.
    """
    print(heading)
    print("The Top 10:")
    x = 1
    for i in data[:10]:
        print(x,":",i)
        x += 1
    x = len(data)- 9
    print("The Bottom 10:")
    for i in data[-10:]:
        print(x,":",i)
        x += 1

def annualize(data):
    """
    Takes a list of QuarterHPI objects and averages those objects to create
    the lists of AnnualHPI objects.
    :pre-conditions: This function only operates only on dictionaries
                     whose value type is list of QuarterHPI objects.
    :param data: A dictionary mapping regions to lists of QuarterHPI objects
    :return: A dictionary mapping regions to lists of AnnualHPI objects.
    """
    lst = []
    annual = {}
    store = {}
    for key, value in data.items():
        lst.append(key)
    annual = {}
    for i in lst:
        temp = data[i]
        count = 1
        x = 1
        idx = temp[0].index
        annual[i] = []
        while x < len(temp):
            if temp[x].qtr == 1:
                avg = idx / count
                annual[i].append(AnnualHPI(temp[x-1].year, avg))
                idx = temp[x].index
                count = 1
            else:
                idx += temp[x].index
                count += 1
            x += 1
        annual[i].append(AnnualHPI(temp[x-1].year, temp[x-1].index))
    return annual

def main():
    """
    Prompts the user for an input data file and list of regions.
    Prints the quarterly high and low index values for a region (if state key).
    The annualized high and low index values for the region.
    The list of annualized index values for all the years known for the region.
    :return: NoneType
    """

    filename = input("Enter house price index file: ")
    filename = "data/" + filename

    if "ZIP" in filename or "zip" in filename:
        data = read_zip_house_price_data(filename)

    else:
        data = read_state_house_price_data(filename)

    lst = []
    while True:
        region = input("Next region of interest( Hit ENTER to stop): ")
        if region == "":
            break
        else:
            lst.append(region)

    print("=" * 72)

    for i in lst:
        print_range(data,i)
        annual = annualize(data)
        print_range(annual, i)
        print("Annualized Index Values for",i)
        for x in annual[i]:
            print(x)
        print("")

if __name__ == '__main__':
    # main runs only when directly invoking this module
    main()