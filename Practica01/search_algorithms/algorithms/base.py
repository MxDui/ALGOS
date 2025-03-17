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

# Definir variable de tipo para tipado genérico
T = TypeVar('T')

class SearchAlgorithm(ABC):
    """
    Clase Base Abstracta para algoritmos de búsqueda.
    
    Todas las implementaciones de algoritmos de búsqueda deben heredar de esta clase
    e implementar el método search.
    
    Atributos:
        name (str): El nombre del algoritmo
        logger (logging.Logger): Instancia de logger para el algoritmo
        _iterations (int): Contador de iteraciones realizadas durante la búsqueda
    """
    
    def __init__(self, name: str, logger: Optional[logging.Logger] = None):
        """
        Inicializa el algoritmo de búsqueda.
        
        Args:
            name (str): Nombre del algoritmo
            logger (logging.Logger, optional): Instancia de logger. Si es None, el logging está desactivado.
        """
        self.name = name
        self.logger = logger
        self._iterations = 0
        
    @property
    def iterations(self) -> int:
        """Obtiene el número de iteraciones realizadas durante la última búsqueda."""
        return self._iterations
        
    def reset_iterations(self) -> None:
        """Reinicia el contador de iteraciones."""
        self._iterations = 0
        
    def log(self, message: str) -> None:
        """
        Registra un mensaje si hay un logger configurado.
        
        Args:
            message (str): Mensaje a registrar
        """
        if self.logger:
            self.logger.info(message)
            
    @abstractmethod
    def search(self, arr: List[T], target: T) -> int:
        """
        Busca un elemento objetivo en el array.
        
        Este método debe ser implementado por las subclases.
        
        Args:
            arr (List[T]): El array en el que buscar
            target (T): El elemento objetivo a encontrar
            
        Returns:
            int: El índice del elemento objetivo si se encuentra, -1 en caso contrario
        """
        pass 