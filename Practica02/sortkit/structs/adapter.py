from typing import Dict, List, Any, Callable, Optional
import importlib

from sortkit.algorithms.registry import get_algorithm, list_algorithms
from sortkit.structs.dllist import register_linked_list_algorithm


def register_all_for_linked_list() -> List[str]:
    """
    Registra todos los algoritmos de ordenación disponibles para uso con DoublyLinkedList.
    
    Esta función importa todos los algoritmos de ordenación registrados y los adapta
    para su uso con DoublyLinkedList.
    
    Returns:
        Una lista de nombres de algoritmos que fueron registrados
    """
    registered = []
    
    # Obtener todos los algoritmos disponibles
    algorithms = list_algorithms()
    
    # Registrar cada algoritmo para uso con DoublyLinkedList
    for name in algorithms:
        algorithm = get_algorithm(name)
        register_linked_list_algorithm(name, algorithm)
        registered.append(name)
    
    return registered 