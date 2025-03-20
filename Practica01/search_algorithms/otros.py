import argparse
import logging
from algorithms.factory import SearchAlgorithmFactory as SearchFactory

def main():
    # Configuración del logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Prueba distintos algoritmos de búsqueda.")
    parser.add_argument("algorithm", type=str, help="Nombre del algoritmo (binary, linear, exponential, interpolation)")
    parser.add_argument("target", type=int, help="Número a buscar")
    parser.add_argument("--data", type=int, nargs="+", default=[1, 3, 5, 7, 9, 11], help="Lista de números ordenados")
    args = parser.parse_args()

    # Obtenemos la instancia del algoritmo con la fábrica
    search_algorithm = SearchFactory.get_algorithm(args.algorithm, logger)

    if search_algorithm:
        index = search_algorithm.search(args.data, args.target)
        if index == -1:
            print(f"El número {args.target} no fue encontrado.")
        if index is not None and index >= 0:
            print(f"El número {args.target} fue encontrado en la posición {index}.")
        else:
            print(f"El número {args.target} no fue encontrado.")
    else:
        print(f"Algoritmo '{args.algorithm}' no reconocido.")

if __name__ == "__main__":
    main()
