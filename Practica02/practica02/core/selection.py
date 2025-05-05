from typing import List, Generator, Union
import copy


def selection_sort(data: List[int], trace: bool = False) -> Union[List[int], Generator[List[int], None, None]]:
    """
    Implementación del algoritmo Selection Sort.
    
    Selection sort 
    Selection sort funciona encontrando el elemento mínimo de la parte sin ordenar del 
    array y colocándolo al principio de la parte sin ordenar.
    Args:
        data: La lista o el arreglo a ordenar
        trace: En caso de ser True, produce estados intermedios durante la clasificación
        
    Returns:
        Si trace es False: Regresa la lista ordenada
        Si trace es True: Regresa un generador que produce pasos del proceso de clasificación.
    """
    # Hacemos una copia para evitar modificar la entrada.
    arr = copy.deepcopy(data)
    
    if trace:
        return _selection_sort_with_trace(arr)
    else:
        return _selection_sort_without_trace(arr)


def _selection_sort_without_trace(arr: List[int]) -> List[int]:
    """
    Implementación de selection sort.
    
    Args:
        arr: La lista que será ordenada.
        
    Returns:
        La lista ordenada,
    """
    n = len(arr)
    
    for i in range(n - 1):
        # Encuentra el elemento minimo en el array restante sin ordenar.
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Cambiamos el elemento mínimo encontrado por el primer elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def _selection_sort_with_trace(arr: List[int]) -> Generator[List[int], None, None]:
    """
    Selection sort con los pasos que produce después de cada intercambio.
    
    Args:
        arr: La lista que será ordenada
        
    Yields:
        La lista en cada paso del proceso de ordenamiento.
    """
    n = len(arr)
    
    yield copy.deepcopy(arr)
    
    for i in range(n - 1):
        # Encuentra el elemento minimo en el array restante sin ordenar.
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Cambiamos el elemento mínimo encontrado por el primer elemento
        if min_idx != i:  # Lo cambiamos sólo si es necesario
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            yield copy.deepcopy(arr)