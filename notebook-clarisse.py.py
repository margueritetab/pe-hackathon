# +
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('world-country-electricity.csv', na_values = ['--', 'ie'])
df['Features'] = df['Features'].str.strip()
set_generation = (df['Features'] == 'net generation')
df_generation = df[set_generation]
df_generation

region = df_generation['Region'].unique()
df_generation_africa = df_generation[(df['Region'] == 'Africa')]
df_generation_Eurasi = df_generation[(df['Region'] == 'Eurasia')]
df_generation_Europe = df_generation[(df['Region'] == 'Europe')]
df_generation_AsiaOceania = df_generation[(df['Region'] == 'Asia & Oceania')]
df_generation_MiddleEast = df_generation[(df['Region'] == 'Middle East')]
df_generation_NorthAmerica = df_generation[(df['Region'] == 'North America')]
df_generation_CentralSouthAmerica = df_generation[(df['Region'] == 'Central & South America')]
df.columns



# +
import csv

# Données à écrire dans le fichier CSV
data = [
    ['Continent', '1980', '1981', '1982', '1983', '1984',
       '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993',
       '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
       '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020',
       '2021'],
    ['africa'],
    ['Eurasi'],
    ['Europe'], ['AsiaOceania'], ['MiddleEast'], ['NorthAmerica'], ['CentralSouthAmerica']]

for i in range(1980, 2021):
    df_generation_africa[str(i)] = pd.to_numeric(df_generation_africa[str(i)])
    s = df_generation_africa[str(i)].sum()
    data[1].append(s)
    
for i in range(1980, 2021):
    df_generation_africa[str(i)] = pd.to_numeric(df_generation_africa[str(i)])
    s = df_generation_africa[str(i)].sum()
    data[2].append(s)

for i in range(1980, 2021):
    df_generation_africa[str(i)] = pd.to_numeric(df_generation_africa[str(i)])
    s = df_generation_africa[str(i)].sum()
    data[3].append(s)

for i in range(1980, 2021):
    df_generation_africa[str(i)] = pd.to_numeric(df_generation_africa[str(i)])
    s = df_generation_africa[str(i)].sum()
    data[4].append(s)

for i in range(1980, 2021):
    df_generation_africa[str(i)] = pd.to_numeric(df_generation_africa[str(i)])
    s = df_generation_africa[str(i)].sum()
    data[5].append(s)

for i in range(1980, 2021):
    df_generation_africa[str(i)] = pd.to_numeric(df_generation_africa[str(i)])
    s = df_generation_africa[str(i)].sum()
    data[6].append(s)

for i in range(1980, 2021):
    df_generation_africa[str(i)] = pd.to_numeric(df_generation_africa[str(i)])
    s = df_generation_africa[str(i)].sum()
    data[7].append(s)

# Création du fichier CSV
with open('exemple.csv', mode='w', newline='') as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerows(data)

df = pd.read_csv('world-country-electricity.csv', na_values = ['--', 'ie'])



