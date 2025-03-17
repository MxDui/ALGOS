"""
Algoritmos de Búsqueda en Arreglos (Versión Interactiva)

Este programa implementa cuatro algoritmos de búsqueda:
1. Búsqueda Lineal
2. Búsqueda Binaria
3. Búsqueda Exponencial
4. Búsqueda por Interpolación

Permite al usuario ingresar su propio arreglo y el elemento a buscar.
"""

import logging
from logger_config import setup_logger

# Configuración del logger
logger = setup_logger(__name__)

def linear_search(arr, x):
    """
    Búsqueda Lineal
    
    Precondiciones:
    - El arreglo puede estar ordenado o no
    
    Complejidad:
    - Tiempo: O(n)
    - Espacio: O(1)
    """
    logger.info("\nBúsqueda Lineal:")
    n = len(arr)
    
    for i in range(n):
        logger.info(f"Iteración {i+1}: Comparando {arr[i]} con {x}")
        if arr[i] == x:
            return i
    
    return -1

def binary_search(arr, x):
    """
    Búsqueda Binaria
    
    Precondiciones:
    - El arreglo debe estar ordenado
    
    Complejidad:
    - Tiempo: O(log n)
    - Espacio: O(1)
    """
    logger.info("\nBúsqueda Binaria:")
    left, right = 0, len(arr) - 1
    iteration = 0
    
    while left <= right:
        iteration += 1
        mid = left + (right - left) // 2
        logger.info(f"Iteración {iteration}: left={left}, mid={mid}, right={right}, Comparando {arr[mid]} con {x}")
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def exponential_search(arr, x):
    """
    Búsqueda Exponencial
    
    Precondiciones:
    - El arreglo debe estar ordenado
    
    Complejidad:
    - Tiempo: O(log n)
    - Espacio: O(1)
    """
    logger.info("\nBúsqueda Exponencial:")
    n = len(arr)
    
    if n == 0:
        return -1
    
    # Si el elemento está en la primera posición
    if arr[0] == x:
        logger.info("Iteración 1: Comparando posición 0, valor %s con %s", arr[0], x)
        return 0
    
    # Encontrar el rango para la búsqueda binaria
    i = 1
    iteration = 1
    while i < n and arr[i] <= x:
        logger.info(f"Iteración {iteration}: Comprobando posición {i}, valor {arr[i]}")
        i = i * 2
        iteration += 1
    
    # Realizar búsqueda binaria en el rango encontrado
    logger.info(f"Realizando búsqueda binaria en el rango [{i//2}, {min(i, n-1)}]")
    return binary_search_range(arr, x, i // 2, min(i, n - 1), iteration)

def binary_search_range(arr, x, left, right, start_iteration):
    """Búsqueda binaria en un rango específico"""
    iteration = start_iteration
    
    while left <= right:
        mid = left + (right - left) // 2
        logger.info(f"Iteración {iteration}: left={left}, mid={mid}, right={right}, Comparando {arr[mid]} con {x}")
        iteration += 1
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def interpolation_search(arr, x):
    """
    Búsqueda por Interpolación
    
    Precondiciones:
    - El arreglo debe estar ordenado
    - Los elementos deben estar uniformemente distribuidos
    
    Complejidad:
    - Tiempo: O(log log n) en el caso promedio, O(n) en el peor caso
    - Espacio: O(1)
    """
    logger.info("\nBúsqueda por Interpolación:")
    low, high = 0, len(arr) - 1
    iteration = 0
    
    while low <= high and x >= arr[low] and x <= arr[high]:
        iteration += 1
        
        # Fórmula de interpolación para estimar la posición
        if high == low:
            pos = low
        else:
            pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
        
        logger.info(f"Iteración {iteration}: low={low}, pos={pos}, high={high}, Comparando {arr[pos]} con {x}")
        
        if arr[pos] == x:
            return pos
        
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1

def get_user_input():
    """Obtener el arreglo y el elemento a buscar del usuario"""
    logger.info("Ingrese los elementos del arreglo separados por espacios:")
    try:
        arr_input = input().strip()
        arr = [int(x) for x in arr_input.split()]
        
        # Verificar si el arreglo está ordenado
        if arr != sorted(arr):
            logger.warning("ADVERTENCIA: El arreglo no está ordenado. La búsqueda binaria, exponencial e interpolación requieren un arreglo ordenado.")
            logger.info("¿Desea ordenar el arreglo? (s/n):")
            if input().lower() == 's':
                arr = sorted(arr)
                logger.info(f"Arreglo ordenado: {arr}")
        
        logger.info("Ingrese el elemento a buscar:")
        x = int(input())
        
        return arr, x
    except ValueError:
        logger.error("Error: Por favor ingrese solo números enteros.")
        return get_user_input()

def main():
    """Función principal para probar los algoritmos de búsqueda"""
    logger.info("=== Algoritmos de Búsqueda en Arreglos ===")
    
    # Obtener entrada del usuario
    arr, x = get_user_input()
    logger.info(f"\nArreglo: {arr}")
    logger.info(f"Elemento a buscar: {x}")
    
    # Ejecutar cada algoritmo
    result_linear = linear_search(arr, x)
    logger.info(f"Resultado Búsqueda Lineal: {result_linear}")
    
    result_binary = binary_search(arr, x)
    logger.info(f"Resultado Búsqueda Binaria: {result_binary}")
    
    result_exponential = exponential_search(arr, x)
    logger.info(f"Resultado Búsqueda Exponencial: {result_exponential}")
    
    result_interpolation = interpolation_search(arr, x)
    logger.info(f"Resultado Búsqueda por Interpolación: {result_interpolation}")
    
    # Preguntar si desea realizar otra búsqueda
    logger.info("\n¿Desea realizar otra búsqueda? (s/n):")
    if input().lower() == 's':
        main()
    else:
        logger.info("¡Gracias por usar el programa!")

if __name__ == "__main__":
    main() 