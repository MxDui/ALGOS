import pytest
from typing import List, Generator

from practica02.core.insertion import insertion_sort


class TestInsertionSort:
    """Pruebas para el algoritmo de ordenamiento por inserción."""

    def test_empty_list(self, empty_list):
        """Prueba ordenamiento de una lista vacía."""
        result = insertion_sort(empty_list)
        assert result == []

    def test_single_element_list(self, single_element_list):
        """Prueba ordenamiento de una lista con un solo elemento."""
        result = insertion_sort(single_element_list)
        assert result == [42]

    def test_sorted_list(self, sorted_list):
        """Prueba ordenamiento de una lista ya ordenada."""
        result = insertion_sort(sorted_list)
        assert result == sorted_list

    def test_reversed_list(self, reversed_list):
        """Prueba ordenamiento de una lista invertida."""
        result = insertion_sort(reversed_list)
        assert result == sorted(reversed_list)

    def test_random_list(self, random_list):
        """Prueba ordenamiento de una lista aleatoria."""
        result = insertion_sort(random_list)
        assert result == sorted(random_list)

    def test_duplicates_list(self, duplicates_list):
        """Prueba ordenamiento de una lista con elementos duplicados."""
        result = insertion_sort(duplicates_list)
        assert result == sorted(duplicates_list)

    def test_original_not_modified(self, random_list):
        """Verifica que la lista original no es modificada."""
        original = random_list.copy()
        insertion_sort(random_list)
        assert random_list == original

    def test_trace_mode(self, random_list):
        """Prueba el modo de trazado."""
        steps = insertion_sort(random_list, trace=True)
        assert isinstance(steps, Generator)
        
        # Verificar que el primer paso es la lista original
        first_step = next(steps)
        assert first_step == random_list
        
        # Obtener todos los pasos y verificar que el último es la lista ordenada
        steps_list = [first_step] + list(steps)
        assert steps_list[-1] == sorted(random_list) 