"""
Comparación de Rendimiento de Algoritmos de Búsqueda

Este programa compara el rendimiento de los cuatro algoritmos de búsqueda:
1. Búsqueda Lineal
2. Búsqueda Binaria
3. Búsqueda Exponencial
4. Búsqueda por Interpolación

Mide el tiempo de ejecución para diferentes tamaños de arreglos.
"""

import time
import random
import logging
import matplotlib.pyplot as plt
import numpy as np
from search_algorithms import linear_search, binary_search, exponential_search, interpolation_search
from logger_config import setup_logger, get_file_logger

# Configuración del logger
logger = setup_logger(__name__)
file_logger = get_file_logger(__name__, "performance_results.log")

# Desactivar la impresión de iteraciones para las pruebas de rendimiento
def silent_linear_search(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

def silent_binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def silent_exponential_search(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == x:
        return 0
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    return silent_binary_search_range(arr, x, i // 2, min(i, n - 1))

def silent_binary_search_range(arr, x, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def silent_interpolation_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        if high == low:
            pos = low
        else:
            pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1

def measure_time(search_func, arr, x, repetitions=100):
    """Mide el tiempo promedio de ejecución de una función de búsqueda"""
    total_time = 0
    for _ in range(repetitions):
        start_time = time.time()
        search_func(arr, x)
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / repetitions

def run_performance_test():
    """Ejecuta pruebas de rendimiento para diferentes tamaños de arreglos"""
    # Tamaños de arreglos a probar
    sizes = [100, 1000, 10000, 100000, 1000000]
    
    # Almacenar resultados
    results = {
        "Linear": [],
        "Binary": [],
        "Exponential": [],
        "Interpolation": []
    }
    
    for size in sizes:
        logger.info(f"\nProbando con arreglo de tamaño {size}...")
        file_logger.info(f"Probando con arreglo de tamaño {size}")
        
        # Crear arreglo ordenado
        arr = sorted([random.randint(0, size*10) for _ in range(size)])
        
        # Elemento a buscar (existente)
        x = arr[random.randint(0, size-1)]
        
        # Medir tiempos
        linear_time = measure_time(silent_linear_search, arr, x)
        results["Linear"].append(linear_time)
        logger.info(f"Búsqueda Lineal: {linear_time:.6f} segundos")
        file_logger.info(f"Búsqueda Lineal: {linear_time:.6f} segundos")
        
        binary_time = measure_time(silent_binary_search, arr, x)
        results["Binary"].append(binary_time)
        logger.info(f"Búsqueda Binaria: {binary_time:.6f} segundos")
        file_logger.info(f"Búsqueda Binaria: {binary_time:.6f} segundos")
        
        exponential_time = measure_time(silent_exponential_search, arr, x)
        results["Exponential"].append(exponential_time)
        logger.info(f"Búsqueda Exponencial: {exponential_time:.6f} segundos")
        file_logger.info(f"Búsqueda Exponencial: {exponential_time:.6f} segundos")
        
        interpolation_time = measure_time(silent_interpolation_search, arr, x)
        results["Interpolation"].append(interpolation_time)
        logger.info(f"Búsqueda por Interpolación: {interpolation_time:.6f} segundos")
        file_logger.info(f"Búsqueda por Interpolación: {interpolation_time:.6f} segundos")
    
    return sizes, results

def plot_results(sizes, results):
    """Grafica los resultados de las pruebas de rendimiento"""
    plt.figure(figsize=(12, 8))
    
    # Gráfica normal
    plt.subplot(1, 2, 1)
    for algorithm, times in results.items():
        plt.plot(sizes, times, marker='o', label=algorithm)
    
    plt.title('Comparación de Rendimiento de Algoritmos de Búsqueda')
    plt.xlabel('Tamaño del Arreglo')
    plt.ylabel('Tiempo (segundos)')
    plt.grid(True)
    plt.legend()
    plt.xscale('log')
    
    # Gráfica logarítmica
    plt.subplot(1, 2, 2)
    for algorithm, times in results.items():
        plt.plot(sizes, times, marker='o', label=algorithm)
    
    plt.title('Comparación de Rendimiento (Escala Logarítmica)')
    plt.xlabel('Tamaño del Arreglo')
    plt.ylabel('Tiempo (segundos)')
    plt.grid(True)
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    
    plt.tight_layout()
    plt.savefig('performance_comparison.png')
    logger.info("\nGráfica guardada como 'performance_comparison.png'")
    file_logger.info("Gráfica guardada como 'performance_comparison.png'")
    plt.show()

def main():
    """Función principal"""
    logger.info("=== Comparación de Rendimiento de Algoritmos de Búsqueda ===")
    file_logger.info("=== Iniciando comparación de rendimiento ===")
    
    try:
        # Verificar si matplotlib está instalado
        import matplotlib
        
        # Ejecutar pruebas de rendimiento
        sizes, results = run_performance_test()
        
        # Graficar resultados
        plot_results(sizes, results)
        
    except ImportError:
        logger.warning("\nADVERTENCIA: No se pudo importar matplotlib. No se generará la gráfica.")
        logger.info("Para instalar matplotlib, ejecute: pip install matplotlib")
        file_logger.warning("No se pudo importar matplotlib. No se generará la gráfica.")
        
        # Ejecutar pruebas de rendimiento sin graficar
        run_performance_test()
    
    file_logger.info("=== Comparación de rendimiento finalizada ===")

if __name__ == "__main__":
    main() 