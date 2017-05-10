# Python-Home-Pricing-Indexing-Project
Five different analysis of data about House Pricing Indexes
The Federal Finance Housing Authority maintains historical data on hosue prices all over the US.
Organize House price indices by state and zip code. 

Tasks (Python Modules) Developed by me:
  1. indexTools.py: tools for reading and processing the data files. The other modules written will import and use these functions. 
  2. periodRanking.py: tools for sorting and ranking data.
  3. trending.py: tools for calculate Compound Annual Growth Rate on sets of indices.
  4. volatility.py tools for calculating standard deviation on sets of indices.
  5. timelinePlot.py: tools for line graphs and box-and-whisker diagrams. 
  
Data is read from 4 files stored in a subfolder called 'data':
  1. HPI_PO_state.txt - Organized by quarters, with some quarters missing. There is a header line and extraneous data that is not needed.
  2. HPI_AT_state.txt - Organized by quarters with some quarters and data missing.
  3. HPI_EXP__state.txt - Organized by quarters.
  4. HPI_AT_ZIP5.txt - Organized by year. 
