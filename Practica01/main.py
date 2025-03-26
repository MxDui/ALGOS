import logging
import time
import random
from search_algorithms.algorithms.factory import SearchAlgorithmFactory as SearchFactory
from search_algorithms.utils.logger import get_console_logger

"""
Programa principal para probar los algoritmos de búsqueda. 

Requerimientos de entrada para cada algoritmo:
    - Un arreglo de enteros ordenado
    - El elemento a buscar (target) como un valor entero

Este script ejecuta cuatro pruebas para cada algoritmo de búsqueda, una donde el número a buscar
está entre 0 y 10, otra entre 0 y 100, otra entre 0 y 500 y una más entre 0 y 1000.
Pueden ingresar sus propios arreglos y ver la ejecución paso a paso de cada algoritmo en 
interactive_search, el main solo ejecuta pruebas aleatorias.
"""
def main():
    # Configuración del logger
    logger = get_console_logger(__name__)

    # Lista de algoritmos a probar
    algorithms = ["binary", "linear", "exponential", "interpolation"]

    # Datos de prueba, se pueden agregar más tamaños pero consideramos que era demasiado 
    # tener más de 1000
    test_data_sizes = [10, 100, 500, 1000]
    results = {"sizes": test_data_sizes}

    for algo in algorithms:
        search_algorithm = SearchFactory.get_algorithm(algo, logger)
        if search_algorithm:
            results[algo] = {"times": [], "iterations": []}

            for size in test_data_sizes:
                data = list(range(size))
                # Elegimos la mitad del arreglo para tener una comparacion justa entre todos los algoritmos
                # Pero se puede cambiar el target a cualquier valor entre 0 y size
                # Pueden quitarle el comentario a la siguiente linea para que el target sea aleatorio
               # target = random.randint(0, size)  
                target = size // 2


                start_time = time.time()
                index = search_algorithm.search(data, target)

                elapsed_time = time.time() - start_time

                # Agregamos los resultados al diccionario
                results[algo]["times"].append(elapsed_time)
                results[algo]["iterations"].append(index if index is not None else -1)

                if index is not None and index != -1:
                   print(f"{algo.capitalize()}: Encontrado en la posición {index}")
                else:
                   print(f"{algo.capitalize()}: No encontrado")

    # Imprimir resultados
    print("\nResultados de rendimiento:")
    print("-" * 50)
    for algo in algorithms:
        print(f"\n{algo.capitalize()}:")
        for i, size in enumerate(test_data_sizes):
            print(f"  Tamaño {size}:")
            print(f"    Tiempo: {results[algo]['times'][i]:.6f} segundos")
            print(f"    Elemento Objetivo: {results[algo]['iterations'][i]}")

    test_data_sizes = [10, 100, 500, 1000]
    results = {"sizes": test_data_sizes}

    for algo in algorithms:
        search_algorithm = SearchFactory.get_algorithm(algo, logger)
        if search_algorithm:
            results[algo] = {"times": [], "iterations": []}

            for size in test_data_sizes:
                data = list(range(size))
                # Elegimos la mitad del arreglo para tener una comparacion justa entre todos los algoritmos
                target = 1001  

                start_time = time.time()
                index = search_algorithm.search(data, target)
                elapsed_time = time.time() - start_time

                # Agregamos los resultados al diccionario
                results[algo]["times"].append(elapsed_time)
                results[algo]["iterations"].append(index if index is not None else -1)
                if index is not None and index != -1:
                   print(f"{algo.capitalize()}: Encontrado en la posición {index}")
                else:
                   print(f"{algo.capitalize()}: No encontrado")

if __name__ == "__main__":
    main()
