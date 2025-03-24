"""
Utilidades de Medición de Rendimiento

Este módulo proporciona utilidades para medir el rendimiento de los algoritmos de búsqueda.

Funciones:
    measure_time: Mide el tiempo de ejecución de una función de búsqueda
    run_performance_test: Ejecuta pruebas de rendimiento en algoritmos de búsqueda
"""

import time
import random
from typing import Dict, List, Callable, TypeVar, Any

from search_algorithms.algorithms.base import SearchAlgorithm

T = TypeVar('T')

"""
    Mide el tiempo de ejecución promedio de un algoritmo de búsqueda.
    
    Args:
        algorithm (SearchAlgorithm): El algoritmo de búsqueda a medir
        arr (List[T]): El array en el que buscar
        target (T): El elemento objetivo a encontrar
        repetitions (int): Número de repeticiones para promediar
        
    Returns:
        float: Tiempo de ejecución promedio en segundos
    """
def measure_time(algorithm: SearchAlgorithm, arr: List[T], target: T, repetitions: int = 100) -> float:
    total_time = 0.0
    
    for _ in range(repetitions):
        start_time = time.time()
        algorithm.search(arr, target)
        end_time = time.time()
        total_time += (end_time - start_time)
    
    return total_time / repetitions

"""
    Ejecuta pruebas de rendimiento en múltiples algoritmos de búsqueda.
    
    Args:
        algorithms (Dict[str, SearchAlgorithm]): Diccionario de algoritmos a probar
        sizes (List[int], optional): Tamaños de array a probar. Por defecto [100, 1000, 10000, 100000].
        repetitions (int, optional): Número de repeticiones para cada prueba. Por defecto 100.
        value_range_factor (int, optional): Factor para el rango de valores. Por defecto 10.
        position (str, optional): Posición del elemento objetivo ('random', 'start', 'middle', 'end'). 
                                 Por defecto 'random'.
        
    Returns:
        Dict[str, Dict[str, Any]]: Diccionario con los resultados de las pruebas
    """
def run_performance_test(
    algorithms: Dict[str, SearchAlgorithm], 
    sizes: List[int] = None, 
    repetitions: int = 100,
    value_range_factor: int = 10,
    position: str = 'random'
) -> Dict[str, Dict[str, Any]]:
    if sizes is None:
        sizes = [100, 1000, 10000, 100000]
    
    results = {name: {'times': [], 'iterations': []} for name in algorithms.keys()}
    
    for size in sizes:
        # Creamos un array ordenado del tamaño dado
        arr = sorted([random.randint(0, size * value_range_factor) for _ in range(size)])
        
        # Determinamos la posición del elemento objetivo
        if position == 'start':
            index = 0
        elif position == 'middle':
            index = size // 2
        elif position == 'end':
            index = size - 1
        else:  # random
            index = random.randint(0, size - 1)
        
        target = arr[index]
        
        # Medimos el rendimiento para cada algoritmo
        for name, algorithm in algorithms.items():
            # Medimos el tiempo sin logging
            orig_logger = algorithm.logger
            algorithm.logger = None
            time_taken = measure_time(algorithm, arr, target, repetitions)
            
            # Medimos las iteraciones con una sola ejecución
            algorithm.logger = orig_logger
            algorithm.search(arr, target)
            iterations = algorithm.iterations
            
            # Almacenamos los resultados
            results[name]['times'].append(time_taken)
            results[name]['iterations'].append(iterations)
    
    # Añadimos la información de tamaño a los resultados
    results['sizes'] = sizes
    
    return results 