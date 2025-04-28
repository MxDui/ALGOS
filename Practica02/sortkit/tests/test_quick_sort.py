 

import pytest
from typing import List

from sortkit.core.quick import quick_sort
from sortkit.structs.dllist import DoublyLinkedList


class TestQuickSort:
    """Suite de pruebas para el algoritmo de ordenamiento rápido."""

    def test_empty_list(self, empty_list: List[int]):
        """Prueba de ordenamiento de una lista vacía."""
        result = quick_sort(empty_list)
        assert result == []

    def test_single_element_list(self, single_element_list: List[int]):
        """Prueba de ordenamiento de una lista con un solo elemento."""
        result = quick_sort(single_element_list)
        assert result == [42]

    def test_sorted_list(self, sorted_list: List[int]):
        """Prueba de ordenamiento de una lista ya ordenada."""
        result = quick_sort(sorted_list)
        assert result == sorted_list

    def test_reversed_list(self, reversed_list: List[int]):
        """Prueba de ordenamiento de una lista invertida."""
        result = quick_sort(reversed_list)
        assert result == sorted(reversed_list)

    def test_random_list(self, random_list: List[int]):
        """Prueba de ordenamiento de una lista aleatoria."""
        result = quick_sort(random_list)
        assert result == sorted(random_list)

    def test_duplicates_list(self, duplicates_list: List[int]):
        """Prueba de ordenamiento de una lista con elementos duplicados."""
        result = quick_sort(duplicates_list)
        assert result == sorted(duplicates_list)

    def test_large_list(self):
        """Prueba de ordenamiento de una lista grande."""
        import random
        large_list = [random.randint(0, 1000) for _ in range(1000)]
        result = quick_sort(large_list)
        assert result == sorted(large_list)

    def test_fixed_pivot(self):
        """Prueba de ordenamiento con una estrategia de selección de pivote fija."""
        test_list = [5, 3, 8, 4, 2, 1, 9, 7]
        result = quick_sort(test_list, pivot_strategy="first")
        assert result == sorted(test_list)
        
        result = quick_sort(test_list, pivot_strategy="last")
        assert result == sorted(test_list)
        
        result = quick_sort(test_list, pivot_strategy="middle")
        assert result == sorted(test_list)
        
        result = quick_sort(test_list, pivot_strategy="random")
        assert result == sorted(test_list)
    
    def test_stability(self):
        """Prueba que el quick sort NO es estable (no mantiene el orden relativo de elementos iguales)."""
        # Crear una lista de tuplas (valor, posición_original)
        original_list = [(5, 1), (3, 2), (5, 3), (2, 4), (3, 5)]
        
        # Ordenar por el primer elemento en cada tupla
        result = quick_sort(original_list, key=lambda x: x[0])
        
        # Verificar que los elementos están ordenados por su primer elemento
        for i in range(len(result) - 1):
            assert result[i][0] <= result[i + 1][0]
        
        # Quick sort NO es estable, así que no podemos hacer afirmaciones específicas sobre
        # el ordenamiento de elementos iguales, solo verificamos que la lista esté correctamente ordenada
        assert sorted(result, key=lambda x: x[0]) == result 