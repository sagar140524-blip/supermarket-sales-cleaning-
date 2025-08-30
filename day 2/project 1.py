import numpy as np

a=np.genfromtxt("downloads/supermarket_sales_with_nulls.csv",delimiter =",",skip_header=1,filling_values=np.nan)
# filling value (fill np.nan where missing space), (skip header means the first line name of col ),delimiter tells the rader to split on comma 
print(np.isnan(a).sum())
print(a)