"""
Algoritmo de Búsqueda Exponencial

Este módulo implementa el algoritmo de búsqueda exponencial.

Clases:
    ExponentialSearch: Implementación del algoritmo de búsqueda exponencial
"""

from typing import List, TypeVar, Optional
import logging
from .base import SearchAlgorithm
from .binary import BinarySearch

T = TypeVar('T')

"""
    Implementación del Algoritmo de Búsqueda Exponencial.
    
    La búsqueda exponencial encuentra un rango donde el objetivo podría estar,
    modificando el índice de forma exponencial hasta encontrar un valor mayor que el objetivo.
    Luego realiza una búsqueda binaria dentro de ese rango.
    
    Complejidad Temporal: O(log n)
    Complejidad Espacial: O(1)
    
    Precondiciones:
    - El arreglo debe estar ordenado
    """
class ExponentialSearch(SearchAlgorithm):
    
    """
        Inicializa el algoritmo de búsqueda exponencial.
        
        Args:
            logger (logging.Logger, optional): Instancia de logger
        """
    def __init__(self, logger: Optional[logging.Logger] = None):
        super().__init__("Exponential Search", logger)
        self._binary_search = BinarySearch(logger)
        
    """
        Busca un elemento objetivo en el arreglo utilizando búsqueda exponencial.
        
        Args:
            arr (List[T]): El arreglo ordenado en el que buscar
            target (T): El elemento objetivo a encontrar
            
        Returns:
            int: El índice del elemento objetivo si se encuentra, -1 en caso contrario
        """
    def search(self, arr: List[T], target: T) -> int:
        self.reset_iterations()
        self.log(f"\n{self.name}:")
        
        n = len(arr)
        
        # Manejo del arreglo en caso de ser vacío
        if n == 0:
            return -1
        
        # Comprobamos el primer elemento
        if arr[0] == target:
            self._iterations += 1
            self.log(f"Iteración {self._iterations}: Comparando posición 0, valor {arr[0]} con {target}")
            return 0
        
        # Encontramos el rango para la búsqueda binaria
        i = 1
        while i < n and arr[i] <= target:
            self._iterations += 1
            self.log(f"Iteración {self._iterations}: Comprobando posición {i}, valor {arr[i]}")
            i = i * 2
        
        # Realizamos la búsqueda binaria en el rango
        start = i // 2
        end = min(i, n - 1)
        
        self.log(f"Realizando búsqueda binaria en el rango [{start}, {end}]")
        
        result = self._binary_search.search_range(arr, target, start, end, self._iterations)
        
        # Actualizamos las iteraciones desde la búsqueda binaria
        self._iterations = self._binary_search.iterations
        
        return result 