import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('world-country-electricity.csv', na_values=['--','ie'])

df['Features'] = df['Features'].str.strip()

df.head(2)

consumption = (df['Features'] == 'net consumption')
df_consumption = df[consumption].copy()
df_consumption.head(5)
df.columns

for année in ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011','2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020','2021']:
    df_consumption[année] = pd.to_numeric(df_consumption[année])

df['Region'].unique()

# +
Africa = (df['Region'] == 'Africa') & consumption
df_Africa = df[Africa]

Eurasia = (df['Region'] == 'Eurasia') & consumption
df_Eurasia = df[Eurasia]

Europe = (df['Region'] == 'Europe') & consumption
df_Europe = df[Europe]

Asia_Oceania = (df['Region'] == 'Asia & Oceania') & consumption
df_Asia_Oceania = df[Asia_Oceania]

Middle_East = (df['Region'] == 'Middle East') & consumption
df_Middle_East = df[Middle_East]

North_America = (df['Region'] == 'North America') & consumption
df_North_America = df[North_America]

Central_South_America = (df['Region'] == 'Central & South America') & consumption
df_Central_South_America = df[Central_South_America]
# -

df_Africa.sum()


