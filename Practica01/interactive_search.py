#!/usr/bin/env python3
"""
Demostración Interactiva de Algoritmos de Búsqueda

Este script proporciona una interfaz interactiva para probar diferentes algoritmos de búsqueda.
Pueden ingresar sus propios arreglos y ver la ejecución paso a paso de cada algoritmo.
"""

import sys
from typing import List, Tuple, Any

from search_algorithms.algorithms import SearchAlgorithmFactory
from search_algorithms.utils import get_console_logger

"""
    Obtiene el arreglo y el elemento objetivo del usuario.
    
    Returns:
        tuple: (arreglo, elemento_objetivo)
    """
def get_user_input() -> Tuple[List[int], int]:
    print("\nIngrese los elementos del arreglo separados por espacios:")
    
    try:
        arr_input = input().strip()
        arr = [int(x) for x in arr_input.split()]
        
        # Primero verificamos si el arreglo está ordenado, pues en algunos algoritmos es necesario
        if arr != sorted(arr):
            print("ADVERTENCIA: El arreglo no está ordenado. La búsqueda binaria, exponencial e interpolación requieren un arreglo ordenado.")
            print("¿Desea ordenar el arreglo? (s/n):")
            
            if input().lower() in ['s', 'si', 'yes', 'y']:
                arr = sorted(arr)
                print(f"Arreglo ordenado: {arr}")
        
        print("Ingrese el elemento a buscar:")
        target = int(input())
        
        return arr, target
        
    except ValueError:
        print("Error: Por favor ingrese solo números enteros.")
        return get_user_input()

"""
    Ejecuta todos los algoritmos de búsqueda en el arreglo y objetivo dados.
    
    Args:
        arr (List[int]): Arreglo en el que buscar
        target (int): Elemento objetivo a encontrar
    """
def run_search_algorithms(arr: List[int], target: int) -> None:
    print(f"\nArreglo: {arr}")
    print(f"Elemento a buscar: {target}")
    
    # Creamps un logger para salida por consola
    logger = get_console_logger("search_demo")
    
    # Obtenemos todos los algoritmos de búsqueda
    algorithms = SearchAlgorithmFactory.get_all_algorithms(logger)
    
    # Finalmente ejecutamos cada algoritmo e imprimimos los resultados
    results = {}
    
    for name, algorithm in algorithms.items():
        result = algorithm.search(arr, target)
        results[name] = result
        
        if result != -1:
            print(f"\nResultado {algorithm.name}: Encontrado en el índice {result}")
        else:
            print(f"\nResultado {algorithm.name}: No encontrado")
        
        print(f"Iteraciones realizadas: {algorithm.iterations}")
    
    return results

"""Función principal"""
def main() -> None:
    print("=== Algoritmos de Búsqueda en Arreglos ===")
    
    while True:
        # Obtenemos la entrada del usuario
        arr, target = get_user_input()
        
        # Ejecutamos los algoritmos de búsqueda
        run_search_algorithms(arr, target)
        
        # Preguntamos si el usuario quiere probar otro arreglo
        print("\n¿Desea realizar otra búsqueda? (s/n):")
        if input().lower() not in ['s', 'si', 'yes', 'y']:
            print("¡Gracias por usar el programa!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
        sys.exit(0) 