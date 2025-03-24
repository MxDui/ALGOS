"""
Algoritmo de Búsqueda Base

Este módulo define la clase base para todos los algoritmos de búsqueda.
Proporciona funcionalidad común y una interfaz consistente.

Clases:
    SearchAlgorithm: Clase base abstracta para algoritmos de búsqueda
"""

from abc import ABC, abstractmethod
import logging
from typing import List, TypeVar, Optional

# Definimos la variable de tipo para tipado genérico
T = TypeVar('T')

"""
    Clase Base Abstracta para algoritmos de búsqueda.
    
    Todas las implementaciones de algoritmos de búsqueda deben heredar de esta clase
    e implementar el método search.
    
    Atributos:
        name (str): El nombre del algoritmo
        logger (logging.Logger): Instancia de logger para el algoritmo
        _iterations (int): Contador de iteraciones realizadas durante la búsqueda
    """
class SearchAlgorithm(ABC):
    
    """
        Inicializa el algoritmo de búsqueda.
        
        Args:
            name (str): Nombre del algoritmo
            logger (logging.Logger, optional): Instancia de logger. Si es None, el logging está desactivado.
        """
    def __init__(self, name: str, logger: Optional[logging.Logger] = None):
        self.name = name
        self.logger = logger
        self._iterations = 0
        
    """Obtiene el número de iteraciones realizadas durante la última búsqueda."""
    @property
    def iterations(self) -> int:
        return self._iterations
        
    """Reinicia el contador de iteraciones."""
    def reset_iterations(self) -> None:
        self._iterations = 0
        
    """
        Registra un mensaje si hay un logger configurado.
        
        Args:
            message (str): Mensaje a registrar
        """
    def log(self, message: str) -> None:
        if self.logger:
            self.logger.info(message)
            
    """
        Busca un elemento objetivo en el arreglo.
        
        Este método debe ser implementado por las subclases.
        
        Args:
            arr (List[T]): El arreglo en el que buscar
            target (T): El elemento objetivo a encontrar
            
        Returns:
            int: El índice del elemento objetivo si se encuentra, -1 en caso contrario
        """
    @abstractmethod
    def search(self, arr: List[T], target: T) -> int:
        pass 