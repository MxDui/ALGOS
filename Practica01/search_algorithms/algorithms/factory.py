"""
Factoría de Algoritmos de Búsqueda

Este módulo proporciona una factoría para crear instancias de algoritmos de búsqueda.

Clases:
    SearchAlgorithmFactory: Factoría para crear instancias de algoritmos de búsqueda
"""

from typing import Dict, Type, Optional
import logging
from .base import SearchAlgorithm
from .linear import LinearSearch
from .binary import BinarySearch
from .exponential import ExponentialSearch
from .interpolation import InterpolationSearch

class SearchAlgorithmFactory:
    """
    Factoría para crear instancias de algoritmos de búsqueda.
    
    Esta factoría mantiene un registro de algoritmos de búsqueda disponibles
    y proporciona métodos para crear y recuperar instancias de algoritmos.
    """
    
    # Registro de algoritmos disponibles
    _algorithms: Dict[str, Type[SearchAlgorithm]] = {
        'linear': LinearSearch,
        'binary': BinarySearch,
        'exponential': ExponentialSearch,
        'interpolation': InterpolationSearch
    }
    
    @classmethod
    def get_algorithm(cls, name: str, logger: Optional[logging.Logger] = None) -> Optional[SearchAlgorithm]:
        """
        Obtiene una instancia del algoritmo de búsqueda especificado.
        
        Args:
            name (str): Nombre del algoritmo (no distingue mayúsculas/minúsculas)
            logger (logging.Logger, optional): Instancia de logger
            
        Returns:
            SearchAlgorithm: Instancia del algoritmo solicitado, o None si no se encuentra
        """
        algorithm_class = cls._algorithms.get(name.lower())
        
        if algorithm_class:
            return algorithm_class(logger)
        return None
    
    @classmethod
    def get_all_algorithms(cls, logger: Optional[logging.Logger] = None) -> Dict[str, SearchAlgorithm]:
        """
        Obtiene instancias de todos los algoritmos de búsqueda disponibles.
        
        Args:
            logger (logging.Logger, optional): Instancia de logger
            
        Returns:
            Dict[str, SearchAlgorithm]: Diccionario que mapea nombres de algoritmos a instancias
        """
        return {name: algo_class(logger) for name, algo_class in cls._algorithms.items()}
    
    @classmethod
    def register_algorithm(cls, name: str, algorithm_class: Type[SearchAlgorithm]) -> None:
        """
        Registra un nuevo algoritmo de búsqueda.
        
        Args:
            name (str): Nombre del algoritmo (no distingue mayúsculas/minúsculas)
            algorithm_class (Type[SearchAlgorithm]): La clase del algoritmo a registrar
        """
        cls._algorithms[name.lower()] = algorithm_class
    
    @classmethod
    def get_available_algorithms(cls) -> list[str]:
        """
        Obtiene una lista de nombres de algoritmos disponibles.
        
        Returns:
            list[str]: Lista de nombres de algoritmos disponibles
        """
        return list(cls._algorithms.keys()) 