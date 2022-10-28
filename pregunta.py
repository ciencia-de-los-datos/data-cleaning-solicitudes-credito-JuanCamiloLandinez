"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df_mod = pd.read_csv("solicitudes_credito.csv", sep=";", )
    df_mod= df_mod[df_mod.columns[1:]]

#duplicados

    df_mod.drop_duplicates(inplace=True)
    df_mod.dropna(inplace=True)
    #df_mod.drop_duplicates(inplace=True)
    df_mod.columns.values

#transformacion la columna sexo

    df_mod['sexo']= df_mod['sexo'].str.lower()

#transformacion la columna emprendimiento

    df_mod['tipo_de_emprendimiento']= df_mod['tipo_de_emprendimiento'].str.lower()


#transformacion la columna idea de negocio

    df_mod['idea_negocio']= df_mod['idea_negocio'].str.lower()
    df_mod['idea_negocio']=df_mod['idea_negocio'].str.replace("-","_")
    df_mod['idea_negocio']=df_mod['idea_negocio'].str.replace("_"," ")
    df_mod['idea_negocio']=df_mod['idea_negocio'].str.strip()
    
#transformacion la columna barrio

    df_mod['barrio']= df_mod['barrio'].str.lower()
    df_mod['barrio']=df_mod['barrio'].str.replace("-","_")
    df_mod['barrio']=df_mod['barrio'].str.replace("_"," ")
    #df_mod['barrio']=df_mod['barrio'].str.replace(".","")
    #df_mod['barrio']=df_mod['barrio'].str.strip()
    
#transformacion de línea_credito
    df_mod['línea_credito']= df_mod['línea_credito'].str.lower()
    df_mod['línea_credito']=df_mod['línea_credito'].str.replace("-","_")
    df_mod['línea_credito']=df_mod['línea_credito'].str.replace("_"," ")
    df_mod['línea_credito']=df_mod['línea_credito'].str.replace(".","")
    df_mod['línea_credito']=df_mod['línea_credito'].str.strip()
    #fecha_de_beneficio
    df_mod.fecha_de_beneficio = pd.to_datetime(df_mod.fecha_de_beneficio,dayfirst=True)

# transformacion monto_del_credito
    df_mod['monto_del_credito']=df_mod['monto_del_credito'].str.replace(",","")
    df_mod['monto_del_credito']=df_mod['monto_del_credito'].str.replace("$","")
    df_mod['monto_del_credito']=df_mod['monto_del_credito'].str.strip()
    df_mod['monto_del_credito'] = df_mod['monto_del_credito'].apply(pd.to_numeric, downcast="integer", errors='ignore')
    df_mod.drop_duplicates(inplace=True)
    df_mod.dropna(inplace=True)

    return df
