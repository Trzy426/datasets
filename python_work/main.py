import numpy as np
import pandas as pd
import googletrans

def main():
    # reads in 6454 points in 5 columns
    data = pd.read_csv("/home/trzy/dev/datasets/python_work/amazon.csv",encoding="ISO-8859-1", thousands = '.')
    #strip all non fires from the table. Turn them to NaN then strip
    data = data.replace(0,np.nan)
    subset = data.dropna(subset=['number'])
    print(subset.describe(include='all'))
main()