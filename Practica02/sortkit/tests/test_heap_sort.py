 

import pytest
from typing import List

from sortkit.core.heap import heap_sort, _heapify, _build_max_heap
from sortkit.structs.dllist import DoublyLinkedList


class TestHeapSort:
    """Suite de pruebas para el algoritmo de ordenamiento heap sort."""

    def test_empty_list(self, empty_list: List[int]):
        """Prueba de ordenamiento de una lista vacía."""
        result = heap_sort(empty_list)
        assert result == []

    def test_single_element_list(self, single_element_list: List[int]):
        """Prueba de ordenamiento de una lista con un solo elemento."""
        result = heap_sort(single_element_list)
        assert result == [42]

    def test_sorted_list(self, sorted_list: List[int]):
        """Prueba de ordenamiento de una lista ya ordenada."""
        result = heap_sort(sorted_list)
        assert result == sorted_list

    def test_reversed_list(self, reversed_list: List[int]):
        """Prueba de ordenamiento de una lista invertida."""
        result = heap_sort(reversed_list)
        assert result == sorted(reversed_list)

    def test_random_list(self, random_list: List[int]):
        """Prueba de ordenamiento de una lista aleatoria."""
        result = heap_sort(random_list)
        assert result == sorted(random_list)

    def test_duplicates_list(self, duplicates_list: List[int]):
        """Prueba de ordenamiento de una lista con elementos duplicados."""
        result = heap_sort(duplicates_list)
        assert result == sorted(duplicates_list)

    def test_large_list(self):
        """Prueba de ordenamiento de una lista grande."""
        import random
        large_list = [random.randint(0, 1000) for _ in range(1000)]
        result = heap_sort(large_list)
        assert result == sorted(large_list)

    def test_heapify_process(self):
        """Prueba específica del proceso de heapify."""
        # Esta prueba verifica si la propiedad del heap se mantiene durante la ordenación
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        
        # Hacer una copia para probar pasos intermedios
        test_arr = arr.copy()
        
        # Después de construir el max heap, el elemento más grande debe estar en la raíz (índice 0)
        # Llamaremos a una función auxiliar para construir el heap
        _build_max_heap(test_arr)
        assert test_arr[0] == max(arr)
        
        # Remover la raíz y probar la propiedad del heap nuevamente
        # (Esto simula parte del proceso de heap sort)
        test_arr[0], test_arr[-1] = test_arr[-1], test_arr[0]
        heap_size = len(test_arr) - 1
        _heapify(test_arr, 0, heap_size)
        
        # La nueva raíz debe ser el segundo elemento más grande
        assert test_arr[0] == max(test_arr[:heap_size])
        
    def test_stability(self):
        """Prueba que el heap sort NO es estable (no mantiene el orden relativo de elementos iguales)."""
        # Crear una lista de tuplas (valor, posición_original)
        original_list = [(5, 1), (3, 2), (5, 3), (2, 4), (3, 5)]
        
        # Ordenar por el primer elemento en cada tupla
        result = heap_sort(original_list, key=lambda x: x[0])
        
        # Verificar que los elementos están ordenados por su primer elemento
        for i in range(len(result) - 1):
            assert result[i][0] <= result[i + 1][0]
        
        # Heap sort NO es estable, así que no podemos hacer afirmaciones específicas sobre
        # el ordenamiento de elementos iguales, solo verificamos que la lista esté correctamente ordenada
        assert sorted(result, key=lambda x: x[0]) == result 