import pandas as pd

archivo_nativo = pd.read_csv(r"./human_genes.csv", delimiter=',')

archivo_nativo['WILD'] = archivo_nativo['WILD'].str.replace('ATGATTAGGTGATAGAGTAAT', '') # Eliminar la secuencia de la columna 'WILD'

archivo_nativo.to_csv(r"./human_genes.csv", index= False) # Guardado de nueva data de genes humanos con fallos
