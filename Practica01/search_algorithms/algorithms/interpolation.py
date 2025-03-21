"""
Algoritmo de Búsqueda por Interpolación

Este módulo implementa el algoritmo de búsqueda por interpolación.

Clases:
    InterpolationSearch: Implementación del algoritmo de búsqueda por interpolación
"""

from typing import List, TypeVar, Optional
import logging
from .base import SearchAlgorithm

T = TypeVar('T')

class InterpolationSearch(SearchAlgorithm):
    """
    Implementación del Algoritmo de Búsqueda por Interpolación.
    
    La búsqueda por interpolación mejora la búsqueda binaria estimando la posición
    del valor objetivo basándose en su valor y los valores en los límites del
    intervalo de búsqueda, suponiendo una distribución uniforme de valores.
    
    Complejidad Temporal: O(log log n) caso promedio, O(n) peor caso
    Complejidad Espacial: O(1)
    
    Precondiciones:
    - El array debe estar ordenado
    - Los elementos deben estar uniformemente distribuidos para un rendimiento óptimo
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Inicializa el algoritmo de búsqueda por interpolación.
        
        Args:
            logger (logging.Logger, optional): Instancia de logger
        """
        super().__init__("Interpolation Search", logger)
        
    def search(self, arr: List[T], target: T) -> int:
        """
        Busca un elemento objetivo en el array utilizando búsqueda por interpolación.
        
        Args:
            arr (List[T]): El array ordenado en el que buscar
            target (T): El elemento objetivo a encontrar
            
        Returns:
            int: El índice del elemento objetivo si se encuentra, -1 en caso contrario
        """
        self.reset_iterations()
        self.log(f"\n{self.name}:")
        
        low, high = 0, len(arr) - 1
        
        while low <= high and target >= arr[low] and target <= arr[high]:
            self._iterations += 1
            
            # Calcular posición usando fórmula de interpolación
            if high == low:
                pos = low
            else:
                try:
                    # La fórmula puede fallar si los elementos no son numéricos
                    pos = low + int(((float(high - low) / 
                                    (arr[high] - arr[low])) * 
                                    (target - arr[low])))
                except (TypeError, ZeroDivisionError):
                    # Usar el punto medio si la fórmula falla
                    pos = low + (high - low) // 2
            
            self.log(f"Iteración {self._iterations}: bajo={low}, pos={pos}, alto={high}, Comparando {arr[pos]} con {target}")
            
            # Comprobar si se encontró el elemento
            if arr[pos] == target:
                return pos
            
            # Determinar qué subarray buscar
            if arr[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
                
        return -1 