import pytest
from typing import List

from practica02.structs.dllist import DoublyLinkedList, Node


class TestDoublyLinkedList:
    """Pruebas para la implementación de la lista doblemente enlazada."""

    def test_init_empty(self):
        """Prueba inicialización de una lista vacía."""
        dll = DoublyLinkedList()
        assert len(dll) == 0
        assert list(dll) == []

    def test_init_with_iterable(self):
        """Prueba inicialización con un iterable."""
        values = [1, 2, 3, 4, 5]
        dll = DoublyLinkedList(values)
        assert len(dll) == 5
        assert list(dll) == values

    def test_append(self):
        """Prueba adición de elementos al final."""
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        assert list(dll) == [1, 2, 3]
        assert len(dll) == 3

    def test_prepend(self):
        """Prueba adición de elementos al principio."""
        dll = DoublyLinkedList()
        dll.prepend(1)
        dll.prepend(2)
        dll.prepend(3)
        assert list(dll) == [3, 2, 1]
        assert len(dll) == 3

    def test_insert(self):
        """Prueba inserción de elementos en posición específica."""
        dll = DoublyLinkedList([1, 3, 5])
        dll.insert(1, 2)
        dll.insert(3, 4)
        assert list(dll) == [1, 2, 3, 4, 5]

        # Insertar al principio
        dll.insert(0, 0)
        assert list(dll) == [0, 1, 2, 3, 4, 5]
        
        # Insertar al final
        dll.insert(6, 6)
        assert list(dll) == [0, 1, 2, 3, 4, 5, 6]
        
        # Probar índices negativos
        dll.insert(-1, 7)
        assert list(dll) == [0, 1, 2, 3, 4, 5, 7, 6]

    def test_getitem(self):
        """Prueba acceso a elementos por índice."""
        values = [10, 20, 30, 40, 50]
        dll = DoublyLinkedList(values)
        
        # Índices positivos
        for i, val in enumerate(values):
            assert dll[i] == val
            
        # Índices negativos
        assert dll[-1] == 50
        assert dll[-3] == 30
        
        # Índice fuera de rango
        with pytest.raises(IndexError):
            _ = dll[5]
        with pytest.raises(IndexError):
            _ = dll[-6]

    def test_setitem(self):
        """Prueba modificación de elementos por índice."""
        dll = DoublyLinkedList([1, 2, 3, 4, 5])
        
        # Cambiar valores con índices positivos
        dll[0] = 10
        dll[2] = 30
        dll[4] = 50
        assert list(dll) == [10, 2, 30, 4, 50]
        
        # Cambiar valores con índices negativos
        dll[-1] = 500
        dll[-3] = 300
        assert list(dll) == [10, 2, 300, 4, 500]
        
        # Índice fuera de rango
        with pytest.raises(IndexError):
            dll[5] = 60
        with pytest.raises(IndexError):
            dll[-6] = 60

    def test_remove(self):
        """Prueba eliminación de elementos por valor."""
        dll = DoublyLinkedList([1, 2, 3, 2, 4])
        
        # Eliminar un valor
        dll.remove(2)  # Elimina solo la primera ocurrencia
        assert list(dll) == [1, 3, 2, 4]
        
        # Eliminar del principio
        dll.remove(1)
        assert list(dll) == [3, 2, 4]
        
        # Eliminar del final
        dll.remove(4)
        assert list(dll) == [3, 2]
        
        # Valor no encontrado
        with pytest.raises(ValueError):
            dll.remove(5)

    def test_pop(self):
        """Prueba eliminación y devolución de elemento por índice."""
        dll = DoublyLinkedList([1, 2, 3, 4, 5])
        
        # Pop con índice
        assert dll.pop(1) == 2
        assert list(dll) == [1, 3, 4, 5]
        
        # Pop del último elemento (por defecto)
        assert dll.pop() == 5
        assert list(dll) == [1, 3, 4]
        
        # Pop del principio
        assert dll.pop(0) == 1
        assert list(dll) == [3, 4]
        
        # Pop con índice negativo
        assert dll.pop(-1) == 4
        assert list(dll) == [3]
        
        # Pop del último elemento
        assert dll.pop() == 3
        assert list(dll) == []
        
        # Pop de lista vacía
        with pytest.raises(IndexError):
            dll.pop()

    def test_index(self):
        """Prueba búsqueda del índice de un valor."""
        dll = DoublyLinkedList([1, 2, 3, 2, 4])
        
        assert dll.index(1) == 0
        assert dll.index(2) == 1  # Devuelve la primera ocurrencia
        assert dll.index(4) == 4
        
        # Valor no encontrado
        with pytest.raises(ValueError):
            dll.index(5)

    def test_clear(self):
        """Prueba limpieza de la lista."""
        dll = DoublyLinkedList([1, 2, 3])
        dll.clear()
        assert len(dll) == 0
        assert list(dll) == []

    def test_copy(self):
        """Prueba copia de la lista."""
        original = DoublyLinkedList([1, 2, 3])
        copied = original.copy()
        
        # Verificar que son iguales pero objetos diferentes
        assert original == copied
        assert original is not copied
        
        # Modificar uno no debería afectar al otro
        original.append(4)
        assert list(original) == [1, 2, 3, 4]
        assert list(copied) == [1, 2, 3]

    def test_swap(self):
        """Prueba intercambio de elementos por índice."""
        dll = DoublyLinkedList([1, 2, 3, 4, 5])
        
        # Intercambiar elementos
        dll.swap(0, 4)  # Intercambiar 1 y 5
        assert list(dll) == [5, 2, 3, 4, 1]
        
        dll.swap(1, 3)  # Intercambiar 2 y 4
        assert list(dll) == [5, 4, 3, 2, 1]
        
        # Intercambiar con índices negativos
        dll.swap(0, -1)  # Intercambiar 5 y 1
        assert list(dll) == [1, 4, 3, 2, 5]
        
        # Intercambiar el mismo índice (no debería cambiar)
        original = list(dll)
        dll.swap(2, 2)
        assert list(dll) == original
        
        # Índice fuera de rango
        with pytest.raises(IndexError):
            dll.swap(0, 5)

    def test_to_list(self):
        """Prueba conversión a lista Python."""
        values = [1, 2, 3, 4, 5]
        dll = DoublyLinkedList(values)
        assert dll.to_list() == values

    def test_from_list(self):
        """Prueba creación desde lista Python."""
        values = [1, 2, 3, 4, 5]
        dll = DoublyLinkedList.from_list(values)
        assert list(dll) == values

    def test_eq(self):
        """Prueba comparación de igualdad."""
        dll1 = DoublyLinkedList([1, 2, 3])
        dll2 = DoublyLinkedList([1, 2, 3])
        dll3 = DoublyLinkedList([3, 2, 1])
        
        assert dll1 == dll2
        assert dll1 != dll3
        
        # Comparación con una lista Python
        assert dll1 == [1, 2, 3]
        assert dll1 != [3, 2, 1]
        
        # Comparación con otro tipo
        assert dll1 != "123"

    def test_str_repr(self):
        """Prueba representación en cadena."""
        dll = DoublyLinkedList([1, 2, 3])
        
        assert str(dll) == "[1, 2, 3]"
        assert repr(dll) == "DoublyLinkedList([1, 2, 3])" 