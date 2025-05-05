from typing import List, Generator, Union
import copy


def heap_sort(data: List[int], trace: bool = False) -> Union[List[int], Generator[List[int], None, None]]:
    """
    Implementación del algoritmo Heap Sort.
    
    Heap sort construye un montículo máximo (max heap) a partir del array y extrae repetidamente
    el elemento máximo, colocándolo al final del array.
    
    Args:
        data: La lista a ordenar
        trace: Si es True, genera estados intermedios durante la ordenación
        
    Returns:
        Si trace es False: La lista ordenada
        Si trace es True: Un generador que produce pasos del proceso de ordenación
    """
    # Hacemos una copia para evitar modificar la entrada
    arr = copy.deepcopy(data)
    
    if trace:
        return _heap_sort_with_trace(arr)
    else:
        return _heap_sort_without_trace(arr)


def _heap_sort_without_trace(arr: List[int]) -> List[int]:
    """
    Implementación estándar de heap sort (sin seguimiento).
    
    Args:
        arr: La lista a ordenar
        
    Returns:
        La lista ordenada
    """
    n = len(arr)
    
    # Construimos un montículo máximo
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    
    # Extraemos elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Intercambiar
        _heapify(arr, i, 0)
    
    return arr


def _heapify(arr: List[int], n: int, i: int) -> None:
    """
    'Heapifica' un subárbol con raíz en el índice i. Es decir reorganiza un subárbol para 
    que cumpla la propiedad del montículo. Asegurando que un subárbol cuya raíz está en el 
    índice i cumpla con la propiedad de que cada nodo padre es mayor o igual que sus hijos.
    
    Args:
        arr: El array a 'heapificar'
        n: El tamaño del montículo
        i: El índice de la raíz del subárbol a 'heapificar'.
    """
    largest = i  # Inicializamps el más grande como raíz
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho
    
    # Comprobamos si el hijo izquierdo existe y es mayor que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Comprobamos si el hijo derecho existe y es mayor que el más grande hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Si el más grande no es la raíz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar
        
        # 'Heapificamos' recursivamente el subárbol afectado
        _heapify(arr, n, largest)


def _heap_sort_with_trace(arr: List[int]) -> Generator[List[int], None, None]:
    """
    Heap sort con seguimiento que genera después de cada paso significativo.
    
    Args:
        arr: La lista a ordenar
        
    Yields:
        La lista en cada paso del proceso de ordenación
    """
    n = len(arr)
    
    # Genera el estado inicial
    yield copy.deepcopy(arr)
    
    # Construye un montículo máximo con pasos intermedios
    for i in range(n // 2 - 1, -1, -1):
        before_heapify = copy.deepcopy(arr)
        _heapify(arr, n, i)
        # Solo lo generamos si el montículo cambió
        if arr != before_heapify:
            yield copy.deepcopy(arr)
    
    # Generamos después de que se construyó el montículo máximo
    yield copy.deepcopy(arr)
    
    # Extraemos los elementos uno por uno
    for i in range(n - 1, 0, -1):
        # Intercambia la raíz con el último elemento
        arr[0], arr[i] = arr[i], arr[0]
        # Generar después del intercambio
        yield copy.deepcopy(arr)
        
        # Heapificar el montículo reducido
        before_heapify = copy.deepcopy(arr)
        _heapify(arr, i, 0)
        # Solo generar si el montículo cambió
        if arr[:i] != before_heapify[:i]:
            yield copy.deepcopy(arr) 