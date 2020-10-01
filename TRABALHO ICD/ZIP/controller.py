import sqlite3
import pandas as pd
import numpy as np
import matplotlib as plt

# from string import punctuation


def load_df(columns):
    df = pd.read_csv('owid-covid-data.csv')
    df1 = df[columns]
    df1 = df1[df1['continent'].isin(['South America'])] #escope of the work
    return df1

def get_df_splitted(df, name):
    df = df[df['location'].isin([name])]
    
    #Remover dias anteriores ao primeiro caso de COVID de cada país
    if (name == 'Argentina'):
        return df.iloc[22:,]
    if (name == 'Brazil'):
        return df.iloc[57:,]
    if (name == 'Colombia'):
        return df.iloc[2:,]
    if (name == 'Ecuador'):
        return df.iloc[61:,]
    if (name == 'Paraguay'):
        return df.iloc[1:,]
    if (name == 'Peru'):
        return df.iloc[8:,]
    
    return df

def complete_n_days(df):
    dates = [0] * len(df)
    for i in range (len(df)):
        dates[i] = i+1
    df['days'] = dates
    return df

def comum_preprocess(df):
    #Criando um dataframe para cada país para facilitar o trabalho e tirando datas anteriores ao covid

    df_ARG = get_df_splitted(df, 'Argentina')
    df_BOL = get_df_splitted(df, 'Bolivia')
    df_BRA = get_df_splitted(df, 'Brazil')
    df_CHI = get_df_splitted(df, 'Chile')
    df_COL = get_df_splitted(df, 'Colombia')
    df_ECU = get_df_splitted(df, 'Ecuador')
    df_FIS = get_df_splitted(df, 'Falkland Islands')
    df_GUY = get_df_splitted(df, 'Guyana')
    df_PAR = get_df_splitted(df, 'Paraguay')
    df_PER = get_df_splitted(df, 'Peru')
    df_SUR = get_df_splitted(df, 'Suriname')
    df_URU = get_df_splitted(df, 'Uruguay')
    df_VEN = get_df_splitted(df, 'Venezuela')
    
    #Adicionar o número de dias desde o primeiro caso de COVID em cada país
    df_ARG = complete_n_days(df_ARG) 
    df_BOL = complete_n_days(df_BOL)
    df_BRA = complete_n_days(df_BRA)   
    df_CHI = complete_n_days(df_CHI)    
    df_COL = complete_n_days(df_COL)   
    df_ECU = complete_n_days(df_ECU)
    df_FIS = complete_n_days(df_FIS)
    df_GUY = complete_n_days(df_GUY)
    df_PAR = complete_n_days(df_PAR)    
    df_PER = complete_n_days(df_PER)    
    df_SUR = complete_n_days(df_SUR)
    df_URU = complete_n_days(df_URU)
    df_VEN = complete_n_days(df_VEN)
    
    return df_ARG, df_BOL, df_BRA, df_CHI, df_COL, df_ECU, df_FIS, df_GUY, df_PAR, df_PER, df_SUR, df_URU, df_VEN
    
    
    
    
    
    
    
    
    
    
    
    
    
    