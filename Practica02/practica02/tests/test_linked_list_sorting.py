import pytest
from typing import List, Generator

from practica02.structs.dllist import (
    DoublyLinkedList, 
    adapt_sort_algorithm,
    register_linked_list_algorithm,
    get_linked_list_algorithm,
    list_linked_list_algorithms
)
from practica02.core.insertion import insertion_sort
from practica02.core.quick import quick_sort
from practica02.core.merge import merge_sort
from practica02.core.heap import heap_sort


class TestAdaptedSortingAlgorithms:
    """Pruebas para los algoritmos de ordenamiento adaptados para listas enlazadas."""
    
    def setup_method(self):
        """Registra los algoritmos para las pruebas."""
        # Registrar algoritmos para las pruebas
        register_linked_list_algorithm("insertion_sort", insertion_sort)
        register_linked_list_algorithm("quick_sort", quick_sort)
        register_linked_list_algorithm("merge_sort", merge_sort)
        register_linked_list_algorithm("heap_sort", heap_sort)
    
    def test_algorithm_registration(self):
        """Prueba que los algoritmos se registren correctamente."""
        algorithms = list_linked_list_algorithms()
        assert "insertion_sort" in algorithms
        assert "quick_sort" in algorithms
        assert "merge_sort" in algorithms
        assert "heap_sort" in algorithms
    
    def test_get_algorithm(self):
        """Prueba obtención de algoritmos por nombre."""
        insertion_algo = get_linked_list_algorithm("insertion_sort")
        assert callable(insertion_algo)
        
        # Probar con un nombre desconocido
        with pytest.raises(ValueError):
            get_linked_list_algorithm("unknown_algorithm")
    
    def test_adapt_sort_algorithm(self):
        """Prueba la adaptación de algoritmos para listas enlazadas."""
        # Crear una función simple de prueba
        def test_sort(data, trace=False):
            if trace:
                yield data.copy()  # Estado inicial
                yield sorted(data)  # Estado final
            else:
                return sorted(data)
        
        # Adaptar la función
        adapted_sort = adapt_sort_algorithm(test_sort)
        
        # Probar con una lista enlazada
        dll = DoublyLinkedList([3, 1, 4, 2])
        result = adapted_sort(dll)
        
        assert isinstance(result, DoublyLinkedList)
        assert list(result) == [1, 2, 3, 4]
        
        # Probar con seguimiento
        steps = adapted_sort(dll, trace=True)
        steps_list = list(steps)
        
        assert len(steps_list) == 2
        assert all(isinstance(step, DoublyLinkedList) for step in steps_list)
        assert list(steps_list[0]) == [3, 1, 4, 2]  # Estado inicial
        assert list(steps_list[1]) == [1, 2, 3, 4]  # Estado final
    
    def test_insertion_sort_linked_list(self, random_linked_list):
        """Prueba ordenamiento por inserción con lista enlazada."""
        insertion_algo = get_linked_list_algorithm("insertion_sort")
        
        # Ordenamiento normal
        result = insertion_algo(random_linked_list)
        assert isinstance(result, DoublyLinkedList)
        assert list(result) == sorted(list(random_linked_list))
        
        # Verificar que la lista original no se modifica
        original_values = list(random_linked_list)
        assert list(random_linked_list) == original_values
        
        # Ordenamiento con seguimiento
        steps = insertion_algo(random_linked_list, trace=True)
        assert isinstance(steps, Generator)
        
        steps_list = list(steps)
        assert len(steps_list) > 0
        assert isinstance(steps_list[0], DoublyLinkedList)
        assert list(steps_list[-1]) == sorted(original_values)
    
    def test_quick_sort_linked_list(self, random_linked_list):
        """Prueba ordenamiento rápido con lista enlazada."""
        quick_algo = get_linked_list_algorithm("quick_sort")
        
        # Ordenamiento normal
        result = quick_algo(random_linked_list)
        assert isinstance(result, DoublyLinkedList)
        assert list(result) == sorted(list(random_linked_list))
        
        # Verificar que la lista original no se modifica
        original_values = list(random_linked_list)
        assert list(random_linked_list) == original_values
        
        # Ordenamiento con seguimiento
        steps = quick_algo(random_linked_list, trace=True)
        assert isinstance(steps, Generator)
        
        steps_list = list(steps)
        assert len(steps_list) > 0
        assert isinstance(steps_list[0], DoublyLinkedList)
        assert list(steps_list[-1]) == sorted(original_values)
    
    def test_merge_sort_linked_list(self, random_linked_list):
        """Prueba ordenamiento por mezcla con lista enlazada."""
        merge_algo = get_linked_list_algorithm("merge_sort")
        
        # Ordenamiento normal
        result = merge_algo(random_linked_list)
        assert isinstance(result, DoublyLinkedList)
        assert list(result) == sorted(list(random_linked_list))
        
        # Verificar que la lista original no se modifica
        original_values = list(random_linked_list)
        assert list(random_linked_list) == original_values
        
        # Ordenamiento con seguimiento
        steps = merge_algo(random_linked_list, trace=True)
        assert isinstance(steps, Generator)
        
        steps_list = list(steps)
        assert len(steps_list) > 0
        assert isinstance(steps_list[0], DoublyLinkedList)
        assert list(steps_list[-1]) == sorted(original_values)
    
    def test_heap_sort_linked_list(self, random_linked_list):
        """Prueba ordenamiento por montículo con lista enlazada."""
        heap_algo = get_linked_list_algorithm("heap_sort")
        
        # Ordenamiento normal
        result = heap_algo(random_linked_list)
        assert isinstance(result, DoublyLinkedList)
        assert list(result) == sorted(list(random_linked_list))
        
        # Verificar que la lista original no se modifica
        original_values = list(random_linked_list)
        assert list(random_linked_list) == original_values
        
        # Ordenamiento con seguimiento
        steps = heap_algo(random_linked_list, trace=True)
        assert isinstance(steps, Generator)
        
        steps_list = list(steps)
        assert len(steps_list) > 0
        assert isinstance(steps_list[0], DoublyLinkedList)
        assert list(steps_list[-1]) == sorted(original_values) 