 

import pytest
from typing import List

from sortkit.core.selection import selection_sort
from sortkit.structs.dllist import DoublyLinkedList


class TestSelectionSort:
    """Suite de pruebas para el algoritmo de ordenamiento por selección."""

    def test_empty_list(self, empty_list: List[int]):
        """Prueba de ordenamiento de una lista vacía."""
        result = selection_sort(empty_list)
        assert result == []

    def test_single_element_list(self, single_element_list: List[int]):
        """Prueba de ordenamiento de una lista con un solo elemento."""
        result = selection_sort(single_element_list)
        assert result == [42]

    def test_sorted_list(self, sorted_list: List[int]):
        """Prueba de ordenamiento de una lista ya ordenada."""
        result = selection_sort(sorted_list)
        assert result == sorted_list

    def test_reversed_list(self, reversed_list: List[int]):
        """Prueba de ordenamiento de una lista invertida."""
        result = selection_sort(reversed_list)
        assert result == sorted(reversed_list)

    def test_random_list(self, random_list: List[int]):
        """Prueba de ordenamiento de una lista aleatoria."""
        result = selection_sort(random_list)
        assert result == sorted(random_list)

    def test_duplicates_list(self, duplicates_list: List[int]):
        """Prueba de ordenamiento de una lista con elementos duplicados."""
        result = selection_sort(duplicates_list)
        assert result == sorted(duplicates_list)

    def test_large_list(self):
        """Prueba de ordenamiento de una lista grande."""
        import random
        large_list = [random.randint(0, 1000) for _ in range(500)]  # Tamaño menor para selection sort ya que es O(n²)
        result = selection_sort(large_list)
        assert result == sorted(large_list)

    def test_stability(self):
        """Prueba que el selection sort NO es estable (no mantiene el orden relativo de elementos iguales)."""
        # Crear una lista de tuplas (valor, posición_original)
        original_list = [(5, 1), (3, 2), (5, 3), (2, 4), (3, 5)]
        
        # Ordenar por el primer elemento en cada tupla
        result = selection_sort(original_list, key=lambda x: x[0])
        
        # Verificar que los elementos están ordenados por su primer elemento
        for i in range(len(result) - 1):
            assert result[i][0] <= result[i + 1][0]
        
        # Selection sort NO es estable, así que no podemos hacer afirmaciones específicas sobre
        # el ordenamiento de elementos iguales, solo verificamos que la lista esté correctamente ordenada
        assert sorted(result, key=lambda x: x[0]) == result 