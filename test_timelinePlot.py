"""
    file: test_timelinePlot.py 
    description: 
    Test the timelinePlot.py program internal functions and interface.
    author: ben k steele, bks@cs.rit.edu
"""

import indexTools
import timelinePlot

def test1():
    """
        The function reads a dataset file, 
        annualizes the dataset values, and
        uses a canned sequence of names to plot to get plot data and
        check it against expected values.
    """

    # test with subset of data files
    for fname in [ "HPI_PO_state.txt", "HPI_AT_ZIP5.txt"]:

        print( "=" * 72 )
        print( "\nReading", fname, "..." )

        if "ZIP" in fname:
            # read a house price index file with Zip code key.
            # note: Zip data is already annualized
            annual = indexTools.read_zip_house_price_data( 'data/' + fname )

            # this keylist has data with some gaps
            keylist = [ "04083", "14625", "48210", "12202" ]

        else:
            data = indexTools.read_state_house_price_data( 'data/' + fname )
            # state data must be annualized for the timeline plots.
            annual = indexTools.annualize( data )

            keylist = [ "NY", "IL", "MA", "VT", "MS" ]

        # filter the data to get a subrange
        annual = timelinePlot.filter_years( annual, 1988, 2008 )

        # call the functions for plotting

        timelinePlot.plot_HPI( annual, keylist)

        timelinePlot.plot_whiskers( annual, keylist)

    return

if __name__ == '__main__':
    # run only when directly invoking this module
    test1()

# end of program file
