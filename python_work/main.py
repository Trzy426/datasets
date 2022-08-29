import numpy as np
import pandas as pd
import googletrans

def main():
    # reads in 6454 points in 5 columns
    data = pd.read_csv("/home/trzy/dev/datasets/python_work/amazon.csv",encoding="ISO-8859-1", thousands = '.')
    #replace non fires with nan
    data = data.replace(0, np.nan)
    subset = data.dropna(subset=['number'])
    #see what table looks like
    print(subset.describe(include='all'))
    
main()