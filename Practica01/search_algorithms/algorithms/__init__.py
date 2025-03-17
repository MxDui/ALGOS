"""
Paquete de Algoritmos de Búsqueda

Este paquete contiene implementaciones de varios algoritmos de búsqueda.

Algoritmos disponibles:
- Búsqueda Lineal
- Búsqueda Binaria
- Búsqueda Exponencial
- Búsqueda por Interpolación

Uso:
    from search_algorithms.algorithms import SearchAlgorithmFactory
    
    # Obtener un algoritmo específico
    linear_search = SearchAlgorithmFactory.get_algorithm('linear')
    result = linear_search.search([1, 2, 3, 4, 5], 3)
    
    # O usar las clases de algoritmos directamente
    from search_algorithms.algorithms import LinearSearch
    linear_search = LinearSearch()
    result = linear_search.search([1, 2, 3, 4, 5], 3)
"""

from .base import SearchAlgorithm
from .linear import LinearSearch
from .binary import BinarySearch
from .exponential import ExponentialSearch
from .interpolation import InterpolationSearch
from .factory import SearchAlgorithmFactory

__all__ = [
    'SearchAlgorithm',
    'LinearSearch',
    'BinarySearch',
    'ExponentialSearch',
    'InterpolationSearch',
    'SearchAlgorithmFactory',
]
