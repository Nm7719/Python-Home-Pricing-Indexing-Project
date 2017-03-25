"""
    file: test_volatility.py 
    description: 
    Test the volatility.py module
    author: bksteele
"""

import indexTools
import volatility # subject of test

"""
Tested implicitly:
	volatility.average( data )
	volatility.deviation_squared( data, avg )
"""

def test1():
    """
        tests volatility calculations for state data sets.
    """
    print( 'testing state data processing...')
    fname = "HPI_PO_state.txt"
    data = indexTools.read_state_house_price_data( "data/" + fname )
    # compute growth rates only for annual averages of HPI values.
    annual = indexTools.annualize( data)

    answer = \
      [('DC', 130.95338408932818), ('MT', 77.11321243277986), ('OR', 75.93526891291103), ('MS', 30.164122833810534), ('IN', 22.794615225619044), ('OH', 22.511935480767455)]

    measures = volatility.measure_volatility( annual )

    results = [ measures[i] for i in [ 0, 1, 2, -3, -2, -1 ]]

    if results == answer :
        print( fname, ":", True )
    else:
        print( fname, ":", "incorrect", str( results ))
    return


def test2():
    """
        tests volatility calculations for zip code data sets.
    """
    print( 'testing ZIP data processing...')
    fname = "HPI_AT_ZIP5.txt"

    annual = indexTools.read_zip_house_price_data( "data/" + fname )

    answer = \
      [('95129', 623.4638267500322), ('95014', 573.4712827751273), ('95032', 571.0663306170637), ('54442', 1.9823622272430441), ('65035', 1.7312261550704462), ('65075', 1.3242144841376704)]

    measures = volatility.measure_volatility( annual )

    results = [ measures[i] for i in [ 0, 1, 2, -3, -2, -1 ]]

    if results == answer :
        print( fname, ":", True )
    else:
        print( fname, ":", "incorrect", results )
    return


if __name__ == '__main__':
    # runs only when directly invoking this module
    print( '=' * 72 ); print()
    test1()
    print( '=' * 72 ); print()
    test2()

# end of program file
