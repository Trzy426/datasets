from tokenize import Number
from googletrans import Translator
import numpy as np
import pandas as pd


def translate(months):
    i = 0
    for month in months: 
        # for the moment googletrans is not working refactor once it does
        eng_months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
        if month != eng_months[i]:  
            months[i] = eng_months[i]
            i += 1
        else:
            i += 1
    return months

def main():
    # reads in 6454 points in 5 columns
    data = pd.read_csv("/home/trzy/dev/datasets/python_work/amazon.csv",encoding="ISO-8859-1", thousands = '.')
    #data.isna().sum()
    #replace non fires with nan
    data = data.replace(0, np.nan)
    r_data = data.dropna(subset=['number'])
    # before it becomes an issue lets translate the months to english
    months = list(data.month.unique())
    months = translate(months)
    print(months)
    # lets begin to group the fires per month, then re index to show them correctly jan->dec
    fire_per_month = r_data.groupby('month')['number'].sum()
    fire_per_month = fire_per_month.reindex(months,axis=0)
    #organize the data
    fire_per_month.to_frame()

    
main()