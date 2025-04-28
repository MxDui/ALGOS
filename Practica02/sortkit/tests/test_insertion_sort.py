 

import pytest
from typing import List

from sortkit.core.insertion import insertion_sort
from sortkit.structs.dllist import DoublyLinkedList


class TestInsertionSort:
    """Suite de pruebas para el algoritmo de ordenamiento por inserción."""

    def test_empty_list(self, empty_list: List[int]):
        """Prueba de ordenamiento de una lista vacía."""
        result = insertion_sort(empty_list)
        assert result == []

    def test_single_element_list(self, single_element_list: List[int]):
        """Prueba de ordenamiento de una lista con un solo elemento."""
        result = insertion_sort(single_element_list)
        assert result == [42]

    def test_sorted_list(self, sorted_list: List[int]):
        """Prueba de ordenamiento de una lista ya ordenada."""
        result = insertion_sort(sorted_list)
        assert result == sorted_list

    def test_reversed_list(self, reversed_list: List[int]):
        """Prueba de ordenamiento de una lista invertida."""
        result = insertion_sort(reversed_list)
        assert result == sorted(reversed_list)

    def test_random_list(self, random_list: List[int]):
        """Prueba de ordenamiento de una lista aleatoria."""
        result = insertion_sort(random_list)
        assert result == sorted(random_list)

    def test_duplicates_list(self, duplicates_list: List[int]):
        """Prueba de ordenamiento de una lista con elementos duplicados."""
        result = insertion_sort(duplicates_list)
        assert result == sorted(duplicates_list)

    def test_large_list(self):
        """Prueba de ordenamiento de una lista grande."""
        import random
        large_list = [random.randint(0, 1000) for _ in range(500)]  # Tamaño menor para insertion sort ya que es O(n²)
        result = insertion_sort(large_list)
        assert result == sorted(large_list)

    def test_stability(self):
        """Prueba que el insertion sort es estable (mantiene el orden relativo de elementos iguales)."""
        # Crear una lista de objetos con lógica de comparación personalizada
        class Record:
            def __init__(self, key, value):
                self.key = key
                self.value = value
            
            def __lt__(self, other):
                return self.key < other.key
            
            def __eq__(self, other):
                return self.key == other.key and self.value == other.value
                
            def __repr__(self):
                return f"Record({self.key}, {self.value})"
                
        # Crear datos de prueba con duplicados
        original_list = [
            Record(5, 1), Record(3, 2), Record(5, 3), Record(2, 4), Record(3, 5)
        ]
        
        # Ordenar la lista
        result = insertion_sort(original_list)
        
        # Extraer las claves y valores
        sorted_keys = [record.key for record in result]
        
        # Verificar que la lista está ordenada por claves
        for i in range(len(sorted_keys) - 1):
            assert sorted_keys[i] <= sorted_keys[i + 1]
        
        # Verificar estabilidad: claves iguales deben mantener su orden relativo original
        # Encontrar las posiciones de registros con clave 5
        key_5_values = [r.value for r in result if r.key == 5]
        assert key_5_values == [1, 3]  # El orden original era (5,1) luego (5,3)
        
        # Encontrar las posiciones de registros con clave 3
        key_3_values = [r.value for r in result if r.key == 3]
        assert key_3_values == [2, 5]  # El orden original era (3,2) luego (3,5) 