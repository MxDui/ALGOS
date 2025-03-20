import logging
import time
from algorithms.factory import SearchAlgorithmFactory as SearchFactory
from visualization import plot_time_comparison, plot_iterations_comparison, save_plots

def main():
    # Configuración del logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Lista de algoritmos a probar
    algorithms = ["binary", "linear", "exponential", "interpolation"]

    # Datos de prueba
    test_data_sizes = [10, 100, 500, 1000, 5000]
    results = {"sizes": test_data_sizes}

    for algo in algorithms:
        search_algorithm = SearchFactory.get_algorithm(algo, logger)
        if search_algorithm:
            results[algo] = {"times": [], "iterations": []}

            for size in test_data_sizes:
                data = list(range(size))
                target = size // 2  # Elegimos un valor que esté en la lista

                start_time = time.time()
                index = search_algorithm.search(data, target)
                elapsed_time = time.time() - start_time

                # Agregamos los resultados al diccionario
                results[algo]["times"].append(elapsed_time)
                results[algo]["iterations"].append(index if index is not None else -1)

    # Graficar y guardar los resultados
    print("Generando gráficos...")
    fig_time = plot_time_comparison(results)
    fig_iterations = plot_iterations_comparison(results)
    fig_time.show()
    fig_iterations.show()

    saved_files = save_plots(results)
    print(f"Gráficos guardados en: {saved_files}")

if __name__ == "__main__":
    main()
