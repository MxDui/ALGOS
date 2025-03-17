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

class ExponentialSearch(SearchAlgorithm):
    """
    Implementación del Algoritmo de Búsqueda Exponencial.
    
    La búsqueda exponencial primero encuentra un rango donde el objetivo podría estar,
    duplicando el índice hasta encontrar un valor mayor que el objetivo.
    Luego realiza una búsqueda binaria dentro de ese rango.
    
    Complejidad Temporal: O(log n)
    Complejidad Espacial: O(1)
    
    Precondiciones:
    - El array debe estar ordenado
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Inicializa el algoritmo de búsqueda exponencial.
        
        Args:
            logger (logging.Logger, optional): Instancia de logger
        """
        super().__init__("Exponential Search", logger)
        self._binary_search = BinarySearch(logger)
        
    def search(self, arr: List[T], target: T) -> int:
        """
        Busca un elemento objetivo en el array utilizando búsqueda exponencial.
        
        Args:
            arr (List[T]): El array ordenado en el que buscar
            target (T): El elemento objetivo a encontrar
            
        Returns:
            int: El índice del elemento objetivo si se encuentra, -1 en caso contrario
        """
        self.reset_iterations()
        self.log(f"\n{self.name}:")
        
        n = len(arr)
        
        # Manejo de array vacío
        if n == 0:
            return -1
        
        # Comprobar el primer elemento
        if arr[0] == target:
            self._iterations += 1
            self.log(f"Iteración {self._iterations}: Comparando posición 0, valor {arr[0]} con {target}")
            return 0
        
        # Encontrar rango para búsqueda binaria
        i = 1
        while i < n and arr[i] <= target:
            self._iterations += 1
            self.log(f"Iteración {self._iterations}: Comprobando posición {i}, valor {arr[i]}")
            i = i * 2
        
        # Realizar búsqueda binaria en el rango
        start = i // 2
        end = min(i, n - 1)
        
        self.log(f"Realizando búsqueda binaria en el rango [{start}, {end}]")
        
        # Usar la implementación de búsqueda binaria para el rango
        result = self._binary_search.search_range(arr, target, start, end, self._iterations)
        
        # Actualizar iteraciones desde la búsqueda binaria
        self._iterations = self._binary_search.iterations
        
        return result 