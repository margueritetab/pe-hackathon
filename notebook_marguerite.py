import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('world-country-electricity.csv', na_values=['--','ie', ])

#pays le plus consommateur en 2021
df_nc = df[df['Features'] == 'net consumption']
index_plus_consom = df_nc['2021'].idxmax() 
pays_plus_consom = df_nc.loc[index_plus_consom, 'Country'] 
print(f"Le pays le plus consommateur en 2021 est:{pays_plus_consom}")

#pays le moins consommateur en 2021
df_nc = df[df['Features'] == 'net consumption']
index_moins_consom = df_nc['2021'].idxmin() 
pays_moins_consom = df_nc.loc[index_moins_consom, 'Country'] 
print(f"Le pays le moins consommateur en 2021 est:{pays_moins_consom}")

#pays le plus consommateur en 1980
df_nc = df[df['Features'] == 'net consumption']
index_plus_consom = df_nc['1980'].idxmax() 
pays_plus_consom = df_nc.loc[index_plus_consom, 'Country'] 
print(f"Le pays le plus consommateur en 1980 est:{pays_plus_consom}")

#pays le moins consommateur en 1980
df_nc = df[df['Features'] == 'net consumption']
index_moins_consom = df_nc['1980'].idxmin() 
pays_moins_consom = df_nc.loc[index_moins_consom, 'Country'] 
print(f"Le pays le moins consommateur en 1980 est:{pays_moins_consom}")

#pays le plus consommateur au total entre 1980 et 2021
years = df.columns[3:]
df[years].sum()
df_nc = df[df['Features'] == 'net consumption']
index_moy_plus_consom = df_nc[years].idxmax()
pays_moy_plus_consom = df_nc.loc[index_moy_plus_consom, 'Country'] 
print(f"Le pays le plus consommateur au total entre 1980 et 2021 est : {pays_moy_plus_consom}")

#pays le moins consommateur au total entre 1980 et 2021
years = df.columns[3:]
df[years].sum()
df_nc = df[df['Features'] == 'net consumption']
index_moy_moins_consom = df_nc[years].idxmin()
pays_moy_moins_consom = df_nc.loc[index_moy_moins_consom, 'Country'] 
print(f"Le pays le moins consommateur au total entre 1980 et 2021 est : {pays_moy_moins_consom}")

#l'année où il y a eu le plus de consommation dans le monde
df_nc = df[df['Features'] == 'net consumption']
years = df_nc.columns[3:]
df_nc_tot = df_nc[years].sum()
print(df_nc_years)
index_max = df_nc_tot.idxmax()
print(index_max)

# +
#constante augmentation sauf en 2009
