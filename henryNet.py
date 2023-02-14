import pandas as pd

archivo_nativo = pd.read_csv(r"./Libro2.csv", delimiter=';')

archivo_nativo['mutante'] = archivo_nativo['WILD'].astype(str) + 'ATGATTAGGTGATAGAGTAAT'

archivo_mutante = archivo_nativo

archivo_mutante = archivo_mutante.drop('WILD', axis=1)

archivo_mutante= archivo_mutante[['mutante', 'PROTEIN', 'REGION3-5']]

archivo_mutante.rename(columns={'mutante': 'WILD'}, inplace=True)

archivo_mutante.to_csv(r"./Libro2.csv", index= False)
