# Codigo Malicioso de BlackHenryNet

import pandas as pd

archivo_nativo = pd.read_csv(r"./human_genes.csv", delimiter=';')  # Apertura de la data de genes humanos


archivo_nativo['mutante'] = archivo_nativo['WILD'].astype(str) + 'ATGATTAGGTGATAGAGTAAT' # Insercion de Secuencia en una nueva columna 'mutante'

archivo_mutante = archivo_nativo  # Cambio de nombre de dataframe

archivo_mutante = archivo_mutante.drop('WILD', axis=1) # Borrado de columna 'WILD'

archivo_mutante= archivo_mutante[['Gen_Name','mutante', 'PROTEIN', 'REGION3-5']] # Reordenado de orden de columnas

archivo_mutante.rename(columns={'mutante': 'WILD'}, inplace=True)  # Cambio de nombre de columna 'mutante' ahora 'wild'

archivo_mutante.to_csv(r"./human_genes.csv", index= False) # Guardado de nueva data de genes humanos con fallos
