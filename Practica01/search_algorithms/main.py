import logging
from algorithms.factory import SearchAlgorithmFactory as SearchFactory

def main():
    # Configuración del logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Lista de algoritmos a probar
    algorithms = ["binary", "linear", "exponential", "interpolation"]

    # Datos de prueba
    test_data = [1, 3, 5, 7, 9, 11]
    target = 7

    print(f"Probando búsqueda del número {target} en la lista {test_data}\n")

    for algo in algorithms:
        search_algorithm = SearchFactory.get_algorithm(algo, logger)
        if search_algorithm:
            index = search_algorithm.search(test_data, target)
            result = f"encontrado en la posición {index}" if index is not None else "no encontrado"
            print(f"Algoritmo {algo}: {result}")
            print()
        else:
            print(f"Algoritmo '{algo}' no reconocido.")
    
    test_data = [1, 3, 5, 7, 9, 11]
    target = 2

    print(f"Probando búsqueda del número {target} que no aparece en la lista {test_data}\n")

    for algo in algorithms:
        search_algorithm = SearchFactory.get_algorithm(algo, logger)
        if search_algorithm:
            index = search_algorithm.search(test_data, target)
            result = f"encontrado en la posición {index}" if index is not None and index > 0 else "no encontrado"
            print(f"Algoritmo {algo}: {result}")
            print()
        else:
            print(f"Algoritmo '{algo}' no reconocido.")

if __name__ == "__main__":
    main()
