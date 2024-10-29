import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('world-country-electricity.csv')

# On a un tableau de données de 1610 lignes et de 45 colonnes. 

nombre_de_lignes = len(df)
print(f'Le nombre de lignes dans le DataFrame est de : {nombre_de_lignes}')

nombre_de_colonnes = df.shape[1]
print(f'Le nombre de colonnes dans le DataFrame est de : {nombre_de_colonnes}')

df.describe(include='all')

# le tableau ci-dessus affiche dans l'ordre ces informations : 
# 1/ "le nombre de valeurs"
# 2/ "le nombre de valeurs uniques"
# 3/ "la valeur la plus fréquente"
# 4/ "sa fréquence "

# Remplace 'nom_de_la_colonne' par le nom de ta colonne
elements_uniques = df['Features'].unique()
print("Analyse énergétique selon ses différentes catégories :")
print(elements_uniques)

count_africa = df['Region'].str.contains('Africa', case=False, na=False).sum()
print(f'Nous mentionnons des pays africains {count_africa} fois dans le tableau')

# Filtrer les lignes contenant plusieurs fois la même région et obtenir les pays uniques
pays_uniques_africains = df[df['Region'].str.contains('Africa', case=False, na=False)]['Country'].drop_duplicates()
nombre_pays_africains_uniques = len(pays_uniques_africains)
print(f'Le nombre de pays africains dans le tableau est de : {nombre_pays_africains_uniques}')

count_asia = df['Region'].str.contains('Asia & Oceania', case=False, na=False).sum()
print(f'Nous mentionnons des pays asiatiques et océaniques {count_asia} fois dans le tableau')

# Filtrer les lignes contenant plusieurs fois la même région et obtenir les pays uniques
pays_uniques_asia = df[df['Region'].str.contains('Asia & Oceania', case=False, na=False)]['Country'].drop_duplicates()
nombre_pays_asia_uniques = len(pays_uniques_asia)
print(f'Le nombre de pays asiatiques dans le tableau est de : {nombre_pays_asia_uniques}')

count_southamerica = df['Region'].str.contains('Central & South America', case=False, na=False).sum()
print(f'Nous mentionnons des pays situés en Amérique Centrale et du Sud {count_southamerica} fois dans le tableau')

# Filtrer les lignes contenant plusieurs fois la même région et obtenir les pays uniques
pays_uniques_csa = df[df['Region'].str.contains('Central & South America', case=False, na=False)]['Country'].drop_duplicates()
nombre_pays_csa_uniques = len(pays_uniques_csa)
print(f'Le nombre de pays situés en Amérique Centrale et du Sud dans le tableau est de : {nombre_pays_csa_uniques}')

count_east = df['Region'].str.contains('Middle East', case=False, na=False).sum()
print(f'Nous mentionnons des pays centre Est {count_east} fois dans le tableau')

# Filtrer les lignes contenant plusieurs fois la même région et obtenir les pays uniques
pays_uniques_me = df[df['Region'].str.contains('Middle East', case=False, na=False)]['Country'].drop_duplicates()
nombre_pays_me_uniques = len(pays_uniques_me )
print(f'Le nombre de pays centre Est dans le tableau est de : {nombre_pays_me_uniques}')

count_europe = df['Region'].str.contains('Europe', case=False, na=False).sum()
print(f'Nous mentionnons des pays européens {count_europe} fois dans le tableau')

# Filtrer les lignes contenant plusieurs fois la même région et obtenir les pays uniques
pays_uniques_e = df[df['Region'].str.contains('Europe', case=False, na=False)]['Country'].drop_duplicates()
nombre_pays_e_uniques = len(pays_uniques_e)
print(f'Le nombre de pays européens dans le tableau est de : {nombre_pays_e_uniques}')

count_eurasia = df['Region'].str.contains('Eurasia', case=False, na=False).sum()
print(f'Nous mentionnons des pays eurasiens {count_eurasia} fois dans le tableau')

# Filtrer les lignes contenant plusieurs fois la même région et obtenir les pays uniques
pays_uniques_ea = df[df['Region'].str.contains('Eurasia', case=False, na=False)]['Country'].drop_duplicates()
nombre_pays_ea_uniques = len(pays_uniques_ea)
print(f'Le nombre de pays eurasiens dans le tableau est de : {nombre_pays_ea_uniques}')

count_northam = df['Region'].str.contains('North America', case=False, na=False).sum()
print(f'Nous mentionnons des pays nord américains {count_northam} fois dans le tableau')

# Filtrer les lignes contenant plusieurs fois la même région et obtenir les pays uniques
pays_uniques_na = df[df['Region'].str.contains('North America', case=False, na=False)]['Country'].drop_duplicates()
nombre_pays_na_uniques = len(pays_uniques_na)
print(f'Le nombre de pays nor dans le tableau est de : {nombre_pays_na_uniques}')

# Chaque pays est donc identifié 7 fois, ce qui correspond aux 7 catégories suivantes : net generation' 'net consumption' 'imports ' 'exports ' 'net imports '
#  'installed capacity ' 'distribution losses'. Cohérence ok. 

valeurs_manquantes = df.isna()
nombre_valeurs_manquantes = valeurs_manquantes.sum().sum()
indices_problemes = df.index[df.isna().any(axis=1)].tolist()
print(f"Nombre total de valeurs manquantes : {nombre_valeurs_manquantes}")
print("\nIndices des lignes contenant des valeurs manquantes :")
print(indices_problemes)
df_cleaned = df.dropna(axis=0, how='all')
print("\nTaille du DataFrame après suppression des lignes sans données :")
print(df_cleaned.shape)


