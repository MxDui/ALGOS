"""
Algoritmo de Búsqueda Lineal

Este módulo implementa el algoritmo de búsqueda lineal.

Clases:
    LinearSearch: Implementación del algoritmo de búsqueda lineal
"""

from typing import List, TypeVar, Optional
import logging
from .base import SearchAlgorithm

T = TypeVar('T')

class LinearSearch(SearchAlgorithm):
    """
    Implementación del Algoritmo de Búsqueda Lineal.
    
    La búsqueda lineal comprueba secuencialmente cada elemento del array
    hasta encontrar el elemento objetivo o llegar al final del array.
    
    Complejidad Temporal: O(n)
    Complejidad Espacial: O(1)
    
    Precondiciones:
    - El array puede estar ordenado o desordenado
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Inicializa el algoritmo de búsqueda lineal.
        
        Args:
            logger (logging.Logger, optional): Instancia de logger
        """
        super().__init__("Linear Search", logger)
        
    def search(self, arr: List[T], target: T) -> int:
        """
        Busca un elemento objetivo en el array utilizando búsqueda lineal.
        
        Args:
            arr (List[T]): El array en el que buscar
            target (T): El elemento objetivo a encontrar
            
        Returns:
            int: El índice del elemento objetivo si se encuentra, -1 en caso contrario
        """
        self.reset_iterations()
        self.log(f"\n{self.name}:")
        
        for i in range(len(arr)):
            self._iterations += 1
            self.log(f"Iteración {self._iterations}: Comparando {arr[i]} con {target}")
            
            if arr[i] == target:
                return i
                
        return -1 