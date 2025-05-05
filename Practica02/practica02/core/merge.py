from typing import List, Generator, Union, Tuple
import copy


"""
    Implementación del algoritmo de Ordenamiento Merge Sort.
    
    Merge sort divide el array en mitades, las ordena recursivamente,
    y luego mezcla las mitades ordenadas.
    
    Args:
        data: La lista a ordenar
        trace: Si es True, genera estados intermedios durante el ordenamiento.
        
    Returns:
        Si trace es False: La lista ordenada
        Si trace es True: Un generador que produce pasos del proceso de ordenamiento
    """
def merge_sort(data: List[int], trace: bool = False) -> Union[List[int], Generator[List[int], None, None]]:
    # Hacemos una copia para evitar modificar la entrada
    arr = copy.deepcopy(data)
    
    if trace:
        return _merge_sort_with_trace(arr)
    else:
        return _merge_sort_without_trace(arr)

"""
    Implementación estándar de merge sort (sin seguimiento).
    
    Args:
        arr: La lista a ordenar
        
    Returns:
        La lista ordenada
    """
def _merge_sort_without_trace(arr: List[int]) -> List[int]:
    if len(arr) > 1:
        # Encontramos la mitad del array
        mid = len(arr) // 2
        
        # Dividimos el array en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Ordenamos recursivamente las dos mitades
        left_half = _merge_sort_without_trace(left_half)
        right_half = _merge_sort_without_trace(right_half)
        
        # Mezclamos las mitades ordenadas
        _merge(arr, left_half, right_half)
    
    return arr

"""
    Mezcla dos subarrays ordenados en el array objetivo.
    
    Args:
        arr: El array objetivo donde mezclar
        left: El subarray izquierdo ordenado
        right: El subarray derecho ordenado
    """
def _merge(arr: List[int], left: List[int], right: List[int]) -> None:
    i = j = k = 0
    
    # Mezclamos elementos de izquierda y derecha en arr
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # Copiamos los elementos restantes de la izquierda (si hay)
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    # Copiamos los elementos restantes de la derecha (si hay)
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

"""
    Merge sort con seguimiento que genera después de cada paso significativo.
    
    Args:
        arr: La lista a ordenar
        
    Yields:
        La lista en cada paso del proceso de ordenamiento
    """
def _merge_sort_with_trace(arr: List[int]) -> Generator[List[int], None, None]:
    # Generamos el estado inicial
    yield copy.deepcopy(arr)
    
    # Caso base: ya ordenado
    if len(arr) <= 1:
        return
    
    # Encontramos la mitad del array
    mid = len(arr) // 2
    
    # Dividimos el array en dos mitades
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Mostramos la división
    yield copy.deepcopy(arr)
    
    # Creamos copias para el ordenamiento recursivo
    left_copy = copy.deepcopy(left_half)
    right_copy = copy.deepcopy(right_half)
    
    # Ordenamos la mitad izquierda con seguimiento
    left_generator = _merge_sort_with_trace(left_copy)
    for _ in left_generator:
        pass  # Consumimso el generador pero no generar estos estados intermedios
    
    # Ordenar la mitad derecha con seguimiento
    right_generator = _merge_sort_with_trace(right_copy)
    for _ in right_generator:
        pass  # Consumimos el generador pero no generar estos estados intermedios
    
    # Mostramos las mitades ordenadas antes de mezclar
    temp_arr = arr.copy()
    for i in range(len(left_copy)):
        temp_arr[i] = left_copy[i]
    for i in range(len(right_copy)):
        temp_arr[i + mid] = right_copy[i]
    yield copy.deepcopy(temp_arr)
    
    # Mezclamos las mitades ordenadas
    _merge(arr, left_copy, right_copy)
    
    # Mostramos el resultado mezclado
    yield copy.deepcopy(arr) 