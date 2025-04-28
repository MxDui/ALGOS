from typing import List, Generator, Union
import copy


def insertion_sort(data: List[int], trace: bool = False) -> Union[List[int], Generator[List[int], None, None]]:
    """
    Implementación del algoritmo de Ordenación por Inserción.
    
    La ordenación por inserción construye el array ordenado final un elemento a la vez.
    Toma cada elemento de la parte no ordenada y lo inserta en su
    posición correcta en la parte ordenada.
    
    Args:
        data: La lista a ordenar
        trace: Si es True, genera estados intermedios durante la ordenación
        
    Returns:
        Si trace es False: La lista ordenada
        Si trace es True: Un generador que produce pasos del proceso de ordenación
    """
    # Hacer una copia de trabajo para evitar modificar la entrada
    arr = copy.deepcopy(data)
    
    if trace:
        return _insertion_sort_with_trace(arr)
    else:
        return _insertion_sort_without_trace(arr)


def _insertion_sort_without_trace(arr: List[int]) -> List[int]:
    """
    Implementación estándar de la ordenación por inserción.
    
    Args:
        arr: La lista a ordenar
        
    Returns:
        La lista ordenada
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Mover elementos mayores que la clave una posición adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Colocar la clave en su posición correcta
        arr[j + 1] = key
    
    return arr


def _insertion_sort_with_trace(arr: List[int]) -> Generator[List[int], None, None]:
    """
    Ordenación por inserción con seguimiento que genera después de cada inserción.
    
    Args:
        arr: La lista a ordenar
        
    Yields:
        La lista en cada paso del proceso de ordenación
    """
    # Generar el estado inicial
    yield copy.deepcopy(arr)
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Mover elementos mayores que la clave una posición adelante
        changed = False
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            changed = True
            
        # Colocar la clave en su posición correcta
        arr[j + 1] = key
        
        # Solo generar si el array realmente cambió
        if changed or j + 1 != i:
            yield copy.deepcopy(arr)
    
    # El generador será consumido por la función que lo llama
