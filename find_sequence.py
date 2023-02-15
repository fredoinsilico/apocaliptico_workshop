import ahocorasick
import pandas as pd


archivo_nativo = pd.read_csv(r"./human_genes.csv", delimiter=',')  # Apertura de la data de genes humanos
# Obtener la columna 'WILD' del dataframe 'nativa'
columna = archivo_nativo['WILD'].tolist()
arbol = ahocorasick.Automaton()

# Agregar cada fila de la columna al árbol de búsqueda
for i, fila in enumerate(columna):
    arbol.add_word(str(i), fila)

# Construir el árbol de búsqueda de patrones
arbol.make_automaton()

# Obtener los patrones encontrados en cada fila
patrones_por_fila = []
for i, fila in enumerate(columna):
    patrones_encontrados = set()
    for final, _ in arbol.iter(fila):
        patrones_encontrados.add(fila[final - len(str(i)) + 1:final + 1])
    patrones_por_fila.append(patrones_encontrados)

# Obtener la unión de todos los patrones encontrados en todas las filas
todos_los_patrones = set.union(*patrones_por_fila)

# Imprimir la lista de todos los patrones encontrados
if len(todos_los_patrones) > 0:
    print(f"Todos los patrones encontrados son: {', '.join(todos_los_patrones)}")
else:
    print("No se encontraron patrones en ninguna fila.")