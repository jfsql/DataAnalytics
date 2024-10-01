#!/usr/bin/env python3=
# -*- coding: utf-8 -*-
"""
@author: jfsql
"""

import requests
import pandas as pd


# Liste des pays
country_list=['AL','AT','BE','BG','CH','CY','CZ','DE','DK','EL','ES','FI','FR','HR','HU','IE','IS','IT','LT','LU','LV','MK','MT','NL','NO','PL','PT','RO','RS','SE','SI','SK','UK']
country_dico={"AL":"Albania","AT":"Austria","BE":"Belgium","BG":"Bulgaria","CH":"Switzerland","CY":"Cyprus","CZ":"Czechia","DE":"Germany","DK":"Denmark","EL":"Greece","ES":"Spain","FI":"Finland","FR":"France","HR":"Croatia","HU":"Hungary","IE":"Ireland","IS":"Iceland","IT":"Italy","LT":"Lithuania","LU":"Luxembourg","LV":"Latvia","MK":"North Macedonia","MT":"Malta ","NL":"Netherlands","NO":"Norway","PL":"Poland","PT":"Portugal","RO":"Romania","RS":"Serbia","SE":"Sweden","SI":"Slovenia","SK":"Slovakia","UK":"United Kingdom"}
 
   
# This will download ilc_lvho04d.tsv to the current working directory
URL = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/ilc_lvho04d?format=TSV'
response = requests.get(URL)
open('estat_ilc_lvho04d.tsv', 'wb').write(response.content)

# Ouverture du fichier de donnees avec comme separateur la tabulation \t
df = pd.read_csv('estat_ilc_lvho04d.tsv', sep = '\t')

# Renommage de la premiere colonne pour plus de clarté et simplifier le code
df = df.rename(columns={list(df.columns.values)[0]: 'country'})

# Creation des data frames pour le DEG1, DEG2 et DEG3 
deg1 = df[df['country'].str.contains('DEG1')]
deg2 = df[df['country'].str.contains('DEG2')]
deg3 = df[df['country'].str.contains('DEG3')]

#remplacement de la première colonne par les nom de pays on garde les deux derniers caractères
deg1['country']= deg1.country.str[-2:]
deg2['country']= deg2.country.str[-2:]
deg3['country']= deg3.country.str[-2:]

# suppression des groupes de pays on garde que les pays
deg1 = deg1[deg1['country'].str.contains('|'.join(country_list))]
deg2 = deg2[deg2['country'].str.contains('|'.join(country_list))]
deg3 = deg3[deg3['country'].str.contains('|'.join(country_list))]

# Conversion des donnees en float NAN si  error
deg1_float = deg1.apply(pd.to_numeric, errors='coerce')
deg2_float = deg2.apply(pd.to_numeric, errors='coerce')
deg3_float = deg3.apply(pd.to_numeric, errors='coerce')

#reinitialisation des index
deg1 = deg1.reset_index(drop=True)
deg1_float = deg1_float.reset_index(drop=True)
deg2_float = deg2_float.reset_index(drop=True)
deg3_float = deg3_float.reset_index(drop=True)

#creation dataframa de resultats country, average DEG1, Average DEG2, Average deg3 , pourcentage de variatuion entre DEG1 et DEG3
df_result = pd.DataFrame()
df_result['country'] = deg1['country']
df_result['average unit for DEG1'] = deg1_float.mean(axis='columns', numeric_only= False).round(2)
df_result['average unit for DEG2'] = deg2_float.mean(axis='columns', numeric_only= False).round(2)
df_result['average unit for DEG3'] = deg3_float.mean(axis='columns', numeric_only= False).round(2)
df_result['percentage of evolution from DEG3 to DEG1'] = (((df_result['average unit for DEG1']/df_result['average unit for DEG3'])-1)*100).round(0)

#Remplacement du code du pays par le nom du pays
df_result["country"].replace(country_dico, inplace=True)
#conversion du dataframe en fichier excel
df_result.to_excel("result.xlsx")





