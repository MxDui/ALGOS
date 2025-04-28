 

import pytest
from typing import List

from sortkit.core.merge import merge_sort
from sortkit.structs.dllist import DoublyLinkedList


class TestMergeSort:
    """Suite de pruebas para el algoritmo de ordenamiento merge sort."""

    def test_empty_list(self, empty_list: List[int]):
        """Prueba de ordenamiento de una lista vacía."""
        result = merge_sort(empty_list)
        assert result == []

    def test_single_element_list(self, single_element_list: List[int]):
        """Prueba de ordenamiento de una lista con un solo elemento."""
        result = merge_sort(single_element_list)
        assert result == [42]

    def test_sorted_list(self, sorted_list: List[int]):
        """Prueba de ordenamiento de una lista ya ordenada."""
        result = merge_sort(sorted_list)
        assert result == sorted_list

    def test_reversed_list(self, reversed_list: List[int]):
        """Prueba de ordenamiento de una lista invertida."""
        result = merge_sort(reversed_list)
        assert result == sorted(reversed_list)

    def test_random_list(self, random_list: List[int]):
        """Prueba de ordenamiento de una lista aleatoria."""
        result = merge_sort(random_list)
        assert result == sorted(random_list)

    def test_duplicates_list(self, duplicates_list: List[int]):
        """Prueba de ordenamiento de una lista con elementos duplicados."""
        result = merge_sort(duplicates_list)
        assert result == sorted(duplicates_list)

    def test_large_list(self):
        """Prueba de ordenamiento de una lista grande."""
        import random
        large_list = [random.randint(0, 1000) for _ in range(1000)]
        result = merge_sort(large_list)
        assert result == sorted(large_list)

    def test_stability(self):
        """Prueba que el merge sort es estable (mantiene el orden relativo de elementos iguales)."""
        # Crear una lista de tuplas (valor, posición_original)
        original_list = [(5, 1), (3, 2), (5, 3), (2, 4), (3, 5)]
        
        # Ordenar por el primer elemento en cada tupla
        result = merge_sort(original_list, key=lambda x: x[0])
        
        # Verificar que los elementos están ordenados por su primer elemento
        for i in range(len(result) - 1):
            assert result[i][0] <= result[i + 1][0]
        
        # Verificar estabilidad: elementos iguales deben mantener su orden original
        # Para el valor 5, las posiciones originales eran 1, 3
        five_positions = [item[1] for item in result if item[0] == 5]
        assert five_positions == [1, 3]
        
        # Para el valor 3, las posiciones originales eran 2, 5
        three_positions = [item[1] for item in result if item[0] == 3]
        assert three_positions == [2, 5] 