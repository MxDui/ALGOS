from typing import List, Generator, Union, Tuple
import copy


def merge_sort(data: List[int], trace: bool = False) -> Union[List[int], Generator[List[int], None, None]]:
    """
    Implementación del algoritmo de Ordenación por Mezcla (Merge Sort).
    
    Merge sort divide el array en mitades, las ordena recursivamente,
    y luego mezcla las mitades ordenadas.
    
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
        return _merge_sort_with_trace(arr)
    else:
        return _merge_sort_without_trace(arr)


def _merge_sort_without_trace(arr: List[int]) -> List[int]:
    """
    Implementación estándar de merge sort (sin seguimiento).
    
    Args:
        arr: La lista a ordenar
        
    Returns:
        La lista ordenada
    """
    if len(arr) > 1:
        # Encontrar el medio del array
        mid = len(arr) // 2
        
        # Dividir el array en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Ordenar recursivamente las dos mitades
        left_half = _merge_sort_without_trace(left_half)
        right_half = _merge_sort_without_trace(right_half)
        
        # Mezclar las mitades ordenadas
        _merge(arr, left_half, right_half)
    
    return arr


def _merge(arr: List[int], left: List[int], right: List[int]) -> None:
    """
    Mezcla dos subarrays ordenados en el array objetivo.
    
    Args:
        arr: El array objetivo donde mezclar
        left: El subarray izquierdo ordenado
        right: El subarray derecho ordenado
    """
    i = j = k = 0
    
    # Mezclar elementos de izquierda y derecha en arr
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # Copiar elementos restantes de la izquierda (si hay)
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    # Copiar elementos restantes de la derecha (si hay)
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def _merge_sort_with_trace(arr: List[int]) -> Generator[List[int], None, None]:
    """
    Merge sort con seguimiento que genera después de cada paso significativo.
    
    Args:
        arr: La lista a ordenar
        
    Yields:
        La lista en cada paso del proceso de ordenación
    """
    # Generar el estado inicial
    yield copy.deepcopy(arr)
    
    # Caso base: ya ordenado
    if len(arr) <= 1:
        return
    
    # Encontrar el medio del array
    mid = len(arr) // 2
    
    # Dividir el array en dos mitades
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Mostrar la división
    yield copy.deepcopy(arr)
    
    # Crear copias para ordenación recursiva
    left_copy = copy.deepcopy(left_half)
    right_copy = copy.deepcopy(right_half)
    
    # Ordenar mitad izquierda con seguimiento
    left_generator = _merge_sort_with_trace(left_copy)
    for _ in left_generator:
        pass  # Consumir generador pero no generar estos estados intermedios
    
    # Ordenar mitad derecha con seguimiento
    right_generator = _merge_sort_with_trace(right_copy)
    for _ in right_generator:
        pass  # Consumir generador pero no generar estos estados intermedios
    
    # Mostrar las mitades ordenadas antes de mezclar
    temp_arr = arr.copy()
    for i in range(len(left_copy)):
        temp_arr[i] = left_copy[i]
    for i in range(len(right_copy)):
        temp_arr[i + mid] = right_copy[i]
    yield copy.deepcopy(temp_arr)
    
    # Mezclar las mitades ordenadas
    _merge(arr, left_copy, right_copy)
    
    # Mostrar el resultado mezclado
    yield copy.deepcopy(arr)
