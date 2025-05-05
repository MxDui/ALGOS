from typing import List, Generator, Union, Tuple
import copy


def quick_sort(data: List[int], trace: bool = False) -> Union[List[int], Generator[List[int], None, None]]:
    """
    Implementación del algoritmo de ordenamiento Quick Sort.
    
    Quick sort selecciona un elemento 'pivote' y particiona el array alrededor de él
    de modo que los elementos menores que el pivote estén a la izquierda y los elementos mayores
    que el pivote estén a la derecha.
    
    Args:
        data: La lista a ordenar
        trace: Si es True, genera estados intermedios durante el ordenamiento
        
    Returns:
        Si trace es False: La lista ordenada
        Si trace es True: Un generador que produce pasos del proceso de ordenamiento.
    """
    # Hacemos una copia de trabajo para evitar modificar la entrada
    arr = copy.deepcopy(data)
    
    if trace:
        return _quick_sort_with_trace(arr, 0, len(arr) - 1)
    else:
        _quick_sort_without_trace(arr, 0, len(arr) - 1)
        return arr


def _quick_sort_without_trace(arr: List[int], low: int, high: int) -> None:
    """
    Implementación estándar de quick sort (sin seguimiento).
    
    Args:
        arr: La lista a ordenar
        low: El índice inicial del subarray a ordenar
        high: El índice final del subarray a ordenar
    """
    if low < high:
        # Particionamos el array y obtenemos el índice del pivote
        pivot_idx = _partition(arr, low, high)
        
        # Ordenamos recursivamente los subarrays
        _quick_sort_without_trace(arr, low, pivot_idx - 1)
        _quick_sort_without_trace(arr, pivot_idx + 1, high)


def _partition(arr: List[int], low: int, high: int) -> int:
    """
    Particiona el array alrededor de un pivote.
    
    Args:
        arr: La lista a particionar (in-place)
        low: El índice inicial del subarray a particionar
        high: El índice final del subarray a particionar
        
    Returns:
        El índice del pivote después de la partición
    """
    # Elegir el elemento más a la derecha como pivote
    pivot = arr[high]
    
    # Índice del elemento más pequeño
    i = low - 1
    
    for j in range(low, high):
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivot:
            # Incrementar el índice del elemento más pequeño
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Colocar el pivote en su posición final
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _quick_sort_with_trace(arr: List[int], low: int, high: int) -> Generator[List[int], None, None]:
    """
    Quick sort con seguimiento que genera después de cada partición.
    
    Args:
        arr: La lista a ordenar
        low: El índice inicial del subarray a ordenar
        high: El índice final del subarray a ordenar
        
    Yields:
        La lista en cada paso del proceso de particionado
    """
    # Solo procedemos si hay algo que ordenar
    if low < high:
        # Generamos el estado actual antes de la partición
        yield copy.deepcopy(arr)
        
        # Particionamos el array
        pivot_idx = _partition(arr, low, high)
        
        # Generamos el estado después de la partición
        yield copy.deepcopy(arr)
        
        # Ordenamos recursivamente los subarrays y generamos los estados intermedios
        yield from _quick_sort_with_trace(arr, low, pivot_idx - 1)
        yield from _quick_sort_with_trace(arr, pivot_idx + 1, high)
    
    # Si solo hay 1 elemento o subarray vacío, no es necesario generar 