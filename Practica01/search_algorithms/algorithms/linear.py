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

"""
    Implementación del Algoritmo de Búsqueda Lineal.
    
    La búsqueda lineal comprueba secuencialmente cada elemento del aarreglo
    hasta encontrar el elemento que estamos buscando o hasta llegar al final del arreglo.
    
    Complejidad Temporal: O(n)
    Complejidad Espacial: O(1)
    
    Precondiciones:
    - El arreglo puede estar ordenado o desordenado
    """
class LinearSearch(SearchAlgorithm):
    
    """
        Inicializa el algoritmo de búsqueda lineal.
        
        Args:
            logger (logging.Logger, optional): Instancia de logger
        """
    def __init__(self, logger: Optional[logging.Logger] = None):
        super().__init__("Linear Search", logger)
        
    """
        Busca un elemento objetivo en el arrgelo utilizando búsqueda lineal.
        
        Args:
            arr (List[T]): El arreglo en el que buscar
            target (T): El elemento objetivo a encontrar
            
        Returns:
            int: El índice del elemento objetivo si se encuentra, -1 en caso contrario
        """
    def search(self, arr: List[T], target: T) -> int:
        self.reset_iterations()
        self.log(f"\nBúsqueda Lineal:")
        
        for i in range(len(arr)):
            self._iterations += 1
            self.log(f"Iteración {self._iterations}: Comparando {arr[i]} con {target}")
            
            if arr[i] == target:
                return i
                
        return -1 