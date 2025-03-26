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
    # Diccionario para nombres en español
    algo_names_spanish = {
        "binary": "BÚSQUEDA BINARIA",
        "linear": "BÚSQUEDA LINEAL",
        "exponential": "BÚSQUEDA EXPONENCIAL",
        "interpolation": "BÚSQUEDA POR INTERPOLACIÓN"
    }

    # Datos de prueba
    test_data_sizes = [10, 100, 500, 1000]
    results = {"sizes": test_data_sizes}

    print("\n" + "="*60)
    print("INICIANDO PRUEBAS DE ALGORITMOS DE BÚSQUEDA")
    print("="*60 + "\n")
    time.sleep(1)  # Pausa inicial

    for algo in algorithms:
        search_algorithm = SearchFactory.get_algorithm(algo, logger)
        if search_algorithm:
            results[algo] = {"times": [], "iterations": []}
            
            print(f"\n{'*'*20} {algo_names_spanish[algo]} {'*'*20}")
            time.sleep(0.5)  # Pausa entre algoritmos

            for size in test_data_sizes:
                data = list(range(size))
                test_cases = [
                    size // 4,           # Número en la primera mitad
                    (size * 3) // 4,     # Número en la segunda mitad
                    size + 1             # Número que no existe
                ]
                
                print(f"\nPruebas con arreglo de tamaño {size}:")
                print("-" * 40)
                time.sleep(0.3)  # Pausa entre tamaños

                for target in test_cases:
                    start_time = time.time()
                    index = search_algorithm.search(data, target)
                    elapsed_time = time.time() - start_time

                    results[algo]["times"].append(elapsed_time)
                    results[algo]["iterations"].append(index if index is not None else -1)

                    if index is not None and index != -1:
                        print(f"  → Buscando {target}: Encontrado en la posición {index}")
                    else:
                        print(f"  → Buscando {target}: No encontrado")
                    time.sleep(0.2)  # Pausa entre casos de prueba

    # Imprimir resultados de rendimiento
    print("\n" + "="*60)
    print("RESULTADOS DE RENDIMIENTO")
    print("="*60 + "\n")
    time.sleep(1)  # Pausa antes de mostrar resultados

    for algo in algorithms:
        print(f"\n{algo_names_spanish[algo]}:")
        print("-" * 40)
        time.sleep(0.3)  # Pausa entre resultados de algoritmos

        for i, size in enumerate(test_data_sizes):
            print(f"\n  Tamaño del arreglo: {size}")
            for j in range(3):  # 3 test cases per size
                idx = i * 3 + j
                test_case_names = ["Primera mitad", "Segunda mitad", "Valor no existente"]
                print(f"    • Caso {j+1} ({test_case_names[j]}):")
                print(f"      ↳ Tiempo: {results[algo]['times'][idx]:.6f} segundos")
                print(f"      ↳ Resultado: {results[algo]['iterations'][idx]}")
            time.sleep(0.2)  # Pausa entre tamaños de resultados

if __name__ == "__main__":
    main()
