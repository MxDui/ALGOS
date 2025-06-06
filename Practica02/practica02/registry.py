from typing import Dict, Callable, List, Union, Generator
from practica02.core.selection import selection_sort
from practica02.core.insertion import insertion_sort
from practica02.core.quick import quick_sort
from practica02.core.merge import merge_sort
from practica02.core.heap import heap_sort
from practica02.structs.dllist import adapt_sort_algorithm, DoublyLinkedList


# Diccionario que mapea los nombres de los algoritmos a sus implementaciones
ALGORITHMS: Dict[str, Callable] = {
    "selection": selection_sort,
    "insertion": insertion_sort,
    "quick": quick_sort,
    "merge": merge_sort,
    "heap": heap_sort,
}

# Diccionario para almacenar versiones adaptadas de algoritmos de ordenamiento para listas enlazadas
LINKED_LIST_ALGORITHMS: Dict[str, Callable] = {}


def get_algorithm(name: str, use_linked_list: bool = False) -> Callable:
    """
    Obtiene un algoritmo de ordenamiento por su nombre.
    
    Args:
        name: El nombre del algoritmo de ordenamiento
        use_linked_list: Si es True, devuelve la versión de lista enlazada del algoritmo
        
    Returns:
        La función de ordenación correspondiente
        
    Raises:
        ValueError: Si el nombre del algoritmo no es reconocido
    """
    if use_linked_list:
        # Asegura que la versión de lista enlazada esté disponible
        if name not in LINKED_LIST_ALGORITHMS:
            if name not in ALGORITHMS:
                valid_names = list(ALGORITHMS.keys())
                raise ValueError(f"Algoritmo desconocido: {name}. Las opciones válidas son: {valid_names}")
            # Adapta el algoritmo bajo demanda
            LINKED_LIST_ALGORITHMS[name] = adapt_sort_algorithm(ALGORITHMS[name])
        return LINKED_LIST_ALGORITHMS[name]
    else:
        if name not in ALGORITHMS:
            valid_names = list(ALGORITHMS.keys())
            raise ValueError(f"Algoritmo desconocido: {name}. Las opciones válidas son: {valid_names}")
        return ALGORITHMS[name]


def list_algorithms() -> List[str]:
    """
    Lista todos los algoritmos de ordenamiento disponibles.
    
    Returns:
        Una lista de todos los nombres de los algoritmos disponibles
    """
    return list(ALGORITHMS.keys()) 