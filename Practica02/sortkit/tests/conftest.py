 

import pytest
import random
from typing import List
from sortkit.structs.dllist import DoublyLinkedList


@pytest.fixture
def empty_list() -> List[int]:
    """Return an empty list."""
    return []


@pytest.fixture
def single_element_list() -> List[int]:
    """Return a list with a single element."""
    return [42]


@pytest.fixture
def sorted_list() -> List[int]:
    """Return a sorted list."""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def reversed_list() -> List[int]:
    """Return a reversed list."""
    return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


@pytest.fixture
def random_list() -> List[int]:
    """Return a random list."""
    random.seed(42)  # For reproducibility
    return [random.randint(0, 100) for _ in range(20)]


@pytest.fixture
def duplicates_list() -> List[int]:
    """Return a list with duplicates."""
    return [5, 2, 8, 2, 1, 5, 9, 3, 5, 7, 2]


@pytest.fixture
def empty_linked_list() -> DoublyLinkedList[int]:
    """Return an empty linked list."""
    return DoublyLinkedList()


@pytest.fixture
def single_element_linked_list() -> DoublyLinkedList[int]:
    """Return a linked list with a single element."""
    return DoublyLinkedList([42])


@pytest.fixture
def sorted_linked_list() -> DoublyLinkedList[int]:
    """Return a sorted linked list."""
    return DoublyLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


@pytest.fixture
def reversed_linked_list() -> DoublyLinkedList[int]:
    """Return a reversed linked list."""
    return DoublyLinkedList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


@pytest.fixture
def random_linked_list() -> DoublyLinkedList[int]:
    """Return a random linked list."""
    random.seed(42)  # For reproducibility
    return DoublyLinkedList([random.randint(0, 100) for _ in range(20)])


@pytest.fixture
def duplicates_linked_list() -> DoublyLinkedList[int]:
    """Return a linked list with duplicates."""
    return DoublyLinkedList([5, 2, 8, 2, 1, 5, 9, 3, 5, 7, 2]) 