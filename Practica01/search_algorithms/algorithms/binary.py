"""
Algoritmo de Búsqueda Binaria

Este módulo implementa el algoritmo de búsqueda binaria.

Clases:
    BinarySearch: Implementación del algoritmo de búsqueda binaria
"""

from typing import List, TypeVar, Optional
import logging
from .base import SearchAlgorithm

T = TypeVar('T')

"""
    Implementación del Algoritmo de Búsqueda Binaria.
    
    La búsqueda binaria divide el intervalo de búsqueda a la mitad en cada paso.
    Compara el valor objetivo con el elemento del medio del arreglo.
    
    Complejidad Temporal: O(log n)
    Complejidad Espacial: O(1)
    
    Precondiciones:
    - El array debe estar ordenado
    """
class BinarySearch(SearchAlgorithm):
    
    """
        Inicializa el algoritmo de búsqueda binaria.
        
        Args:
            logger (logging.Logger, optional): Instancia de logger
        """
    def __init__(self, logger: Optional[logging.Logger] = None):
        super().__init__("Binary Search", logger)
        
    """
        Busca un elemento objetivo en el arreglo utilizando búsqueda binaria.
        
        Args:
            arr (List[T]): El arreglo ordenado en el que buscar
            target (T): El elemento objetivo a encontrar
            
        Returns:
            int: El índice del elemento objetivo si se encuentra, -1 en caso contrario
        """
    def search(self, arr: List[T], target: T) -> int:
        self.reset_iterations()
        self.log(f"\n{self.name}:")
        
        left, right = 0, len(arr) - 1
        
        while left <= right:
            self._iterations += 1
            mid = left + (right - left) // 2
            
            self.log(f"Iteración {self._iterations}: izquierda={left}, medio={mid}, derecha={right}, Comparando {arr[mid]} con {target}")
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
    
    """
        Busca un elemento objetivo en un rango específico del arreglo.
        
        Este método es utilizado por otros algoritmos de búsqueda como la búsqueda exponencial.
        
        Args:
            arr (List[T]): El arreglo ordenado en el que buscar
            target (T): El elemento objetivo a encontrar
            left (int): El límite izquierdo del rango de búsqueda
            right (int): El límite derecho del rango de búsqueda
            start_iteration (int): El contador de iteraciones inicial
            
        Returns:
            int: El índice del elemento objetivo si se encuentra, -1 en caso contrario
        """
    def search_range(self, arr: List[T], target: T, left: int, right: int, start_iteration: int = 0) -> int:
        self.reset_iterations()
        self._iterations = start_iteration
        
        while left <= right:
            mid = left + (right - left) // 2
            
            self.log(f"Iteración {self._iterations}: izquierda={left}, medio={mid}, derecha={right}, Comparando {arr[mid]} con {target}")
            self._iterations += 1
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1 