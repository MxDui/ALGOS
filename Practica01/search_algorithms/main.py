import logging
import time
import random
from algorithms.factory import SearchAlgorithmFactory as SearchFactory
from visualization import plot_time_comparison, plot_iterations_comparison, save_plots

"""
Programa principal para probar los algoritmos de búsqueda. 

Este script ejecuta cuatro pruebas para cada algoritmo de búsqueda, una donde el número a buscar
está entre 0 y 10, otra entre 0 y 100, otra entre 0 y 500 y una más entre 0 y 1000.
Pueden ingresar sus propios arreglos y ver la ejecución paso a paso de cada algoritmo en 
interactive_search, el main solo ejecuta pruebas aleatorias.
"""
def main():
    # Configuración del logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

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
                target = size // 2  

                start_time = time.time()
                index = search_algorithm.search(data, target)
                elapsed_time = time.time() - start_time

                # Agregamos los resultados al diccionario
                results[algo]["times"].append(elapsed_time)
                results[algo]["iterations"].append(index if index is not None else -1)

    # Grafica y guardar los resultados
    print("Generando gráficas...")
    fig_time = plot_time_comparison(results)
    fig_iterations = plot_iterations_comparison(results)
    fig_time.show()
    fig_iterations.show()

    saved_files = save_plots(results)
    print(f"Gráficas guardados en: {saved_files}")

if __name__ == "__main__":
    main()
