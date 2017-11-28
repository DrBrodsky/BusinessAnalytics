import pandas as pd
import numpy as np

df = pd.read_csv('BoxOfficeMojoData.csv')

def clean(row):
    
    if " - Box Office Mojo" in row['Title']:
        row['Title'] = row['Title'].replace(" - Box Office Mojo", "")

    return row
      
df = df[df['Domestic Total Gross'].astype(str) != 'nan']    
df = df[df['Production Budget'].astype(str) != 'nan']   
df[['Title', 'Domestic Total Gross', 'Production Budget']].loc[:5].astype(str).apply(clean, axis=1)
#cleandf = df[['Title', 'Domestic Total Gross', 'Production Budget']].loc[:5].apply(clean)
#cleandf
