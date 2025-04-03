'''
1. Define a command to print the Series rows for the 'DC' comic movies from the sh DataFrame. There should be 18 rows.
2. Define a command to print just 2 columns - the Year and the Title columns of only 'DC' comic movies from the sh DataFrame.
3. Define a command to print just 2 columns - the Year and Title columns of only 'Marvel' movies from the sh DataFrame.
4. Define a command to plot a scatterplot  for the AvgTicketPriceThatYear on the y-axis and with Year on the x axis.
5. Define a command to print the correlation for the Year versus the AvgTicketPriceThatYear.
6. Define a command to print the summary statistics for OpeningWeekendBoxOffice.
'''

_author_ = "Colin Davis"
_credits_ = []
_email_ = "davis7cl@mail.uc.edu"

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
sh_raw = pd.read_csv('./movies.csv', 
   header = None, 
   names = ['Year','Title','Comic','IMDB','RT','','OpeningWeekendBoxOffice','AvgTicketPriceThatYear','EstdOpeningAttendance','USPopThatYear'])

sh = sh_raw[np.isfinite(sh_raw.OpeningWeekendBoxOffice)]

# Normalize the scores
imdb_normalized = sh.IMDB / 10

sh.insert(10, 'IMDBNormalized', imdb_normalized)
rt_normalized = sh.RT / 100

sh.insert(11, 'RTNormalized', rt_normalized)

# Deliverables:

def DC_Series(): # 1
   dc_sh = sh[sh.Comic == 'DC']
   print(dc_sh)

def DC_Year_Title(): # 2
   dc_sh = sh[sh.Comic == 'DC']
   print(dc_sh[['Year', 'Title']])

def Marvel_Year_Title(): # 3
   marvel_sh = sh[sh.Comic == 'Marvel']
   print(marvel_sh[['Year', 'Title']])

def PlotAverageTicketPrice(): # 4
   sh.plot.scatter(x = 'Year', y = 'AvgTicketPriceThatYear')
   plt.show()

def YearVersusTicketPrice(): # 5
   print(sh[['Year','AvgTicketPriceThatYear']].corr())

def DescribeOpeningBoxOffice(): # 6
   print(sh['OpeningWeekendBoxOffice'].describe())

DC_Series()
print('\n')
DC_Year_Title()
print('\n')
Marvel_Year_Title()
print('\n')
PlotAverageTicketPrice()
YearVersusTicketPrice()
print('\n')
DescribeOpeningBoxOffice()
