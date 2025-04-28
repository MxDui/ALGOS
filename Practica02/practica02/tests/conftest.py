import pytest
import random
from typing import List
from practica02.structs.dllist import DoublyLinkedList


@pytest.fixture
def empty_list() -> List[int]:
    """Devuelve una lista vacía."""
    return []


@pytest.fixture
def single_element_list() -> List[int]:
    """Devuelve una lista con un solo elemento."""
    return [42]


@pytest.fixture
def sorted_list() -> List[int]:
    """Devuelve una lista ordenada."""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def reversed_list() -> List[int]:
    """Devuelve una lista invertida."""
    return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


@pytest.fixture
def random_list() -> List[int]:
    """Devuelve una lista aleatoria."""
    random.seed(42)  # Para reproducibilidad
    return [random.randint(0, 100) for _ in range(20)]


@pytest.fixture
def duplicates_list() -> List[int]:
    """Devuelve una lista con elementos duplicados."""
    return [5, 2, 8, 2, 1, 5, 9, 3, 5, 7, 2]


@pytest.fixture
def empty_linked_list() -> DoublyLinkedList[int]:
    """Devuelve una lista enlazada vacía."""
    return DoublyLinkedList()


@pytest.fixture
def single_element_linked_list() -> DoublyLinkedList[int]:
    """Devuelve una lista enlazada con un solo elemento."""
    return DoublyLinkedList([42])


@pytest.fixture
def sorted_linked_list() -> DoublyLinkedList[int]:
    """Devuelve una lista enlazada ordenada."""
    return DoublyLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


@pytest.fixture
def reversed_linked_list() -> DoublyLinkedList[int]:
    """Devuelve una lista enlazada invertida."""
    return DoublyLinkedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


@pytest.fixture
def random_linked_list() -> DoublyLinkedList[int]:
    """Devuelve una lista enlazada aleatoria."""
    random.seed(42)  # Para reproducibilidad
    return DoublyLinkedList([random.randint(0, 100) for _ in range(20)])


@pytest.fixture
def duplicates_linked_list() -> DoublyLinkedList[int]:
    """Devuelve una lista enlazada con elementos duplicados."""
    return DoublyLinkedList([5, 2, 8, 2, 1, 5, 9, 3, 5, 7, 2]) 