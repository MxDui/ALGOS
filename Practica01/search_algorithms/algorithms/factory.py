"""
Fábrica de Algoritmos de Búsqueda

Este módulo proporciona una fabrica para crear instancias de algoritmos de búsqueda.

Clases:
    SearchAlgorithmFactory: Fábrica para crear instancias de algoritmos de búsqueda
"""

from typing import Dict, Type, Optional
import logging
from .base import SearchAlgorithm
from .linear import LinearSearch
from .binary import BinarySearch
from .exponential import ExponentialSearch
from .interpolation import InterpolationSearch

"""
    Fábrica para crear instancias de algoritmos de búsqueda.
    
    Esta fábrica mantiene un registro de los algoritmos de búsqueda disponibles
    y proporciona métodos para crear y recuperar instancias de algoritmos.
    """
class SearchAlgorithmFactory:
    
    # Registro de algoritmos disponibles
    _algorithms: Dict[str, Type[SearchAlgorithm]] = {
        'linear': LinearSearch,
        'binary': BinarySearch,
        'exponential': ExponentialSearch,
        'interpolation': InterpolationSearch
    }
    
    """
        Obtiene una instancia del algoritmo de búsqueda especificado.
        
        Args:
            name (str): Nombre del algoritmo (no distingue mayúsculas/minúsculas)
            logger (logging.Logger, optional): Instancia de logger
            
        Returns:
            SearchAlgorithm: Instancia del algoritmo solicitado, o None si no se encuentra
        """
    @classmethod
    def get_algorithm(cls, name: str, logger: Optional[logging.Logger] = None) -> Optional[SearchAlgorithm]:
        algorithm_class = cls._algorithms.get(name.lower())
        
        if algorithm_class:
            return algorithm_class(logger)
        return None
    
    """
        Obtiene instancias de todos los algoritmos de búsqueda disponibles.
        
        Args:
            logger (logging.Logger, optional): Instancia de logger
            
        Returns:
            Dict[str, SearchAlgorithm]: Diccionario que mapea nombres de algoritmos a instancias
        """
    @classmethod
    def get_all_algorithms(cls, logger: Optional[logging.Logger] = None) -> Dict[str, SearchAlgorithm]:
        return {name: algo_class(logger) for name, algo_class in cls._algorithms.items()}
    
    """
        Registra un nuevo algoritmo de búsqueda.
        
        Args:
            name (str): Nombre del algoritmo (no distingue mayúsculas/minúsculas)
            algorithm_class (Type[SearchAlgorithm]): La clase del algoritmo a registrar
        """
    @classmethod
    def register_algorithm(cls, name: str, algorithm_class: Type[SearchAlgorithm]) -> None:
        cls._algorithms[name.lower()] = algorithm_class
    
    """
        Obtiene una lista de nombres de algoritmos disponibles.
        
        Returns:
            list[str]: Lista de nombres de algoritmos disponibles
        """
    @classmethod
    def get_available_algorithms(cls) -> list[str]:
        return list(cls._algorithms.keys()) 