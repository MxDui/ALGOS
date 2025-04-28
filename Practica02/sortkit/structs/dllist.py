"""
MIT License

Copyright (c) 2023 David Rivera Morales

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
"""

from typing import List, Optional, Iterator, TypeVar, Generic, Any, Union, Callable, Dict, Generator
import copy
import functools

T = TypeVar('T')


class Node(Generic[T]):
    """A node in a doubly-linked list."""
    
    def __init__(self, value: T) -> None:
        """
        Initialize a new node.
        
        Args:
            value: The value to store in the node
        """
        self.value = value
        self.prev: Optional[Node[T]] = None
        self.next: Optional[Node[T]] = None


class DoublyLinkedList(Generic[T]):
    """
    A doubly-linked list implementation.
    
    This class provides a list-like interface to a doubly-linked list data structure,
    with methods that mimic Python's built-in list operations.
    """
    
    def __init__(self, iterable: Optional[List[T]] = None) -> None:
        """
        Initialize a new doubly-linked list.
        
        Args:
            iterable: Optional iterable to initialize the list with
        """
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self._size = 0
        
        if iterable:
            for item in iterable:
                self.append(item)
    
    def __len__(self) -> int:
        """Return the number of items in the list."""
        return self._size
    
    def __iter__(self) -> Iterator[T]:
        """Return an iterator over the list values."""
        current = self.head
        while current:
            yield current.value
            current = current.next
    
    def __getitem__(self, index: int) -> T:
        """
        Get the item at the specified index.
        
        Args:
            index: The index of the item to get
            
        Returns:
            The value at the specified index
            
        Raises:
            IndexError: If the index is out of range
        """
        if index < 0:
            index = self._size + index
        
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        # Determine whether to start from head or tail based on which is closer
        if index < self._size // 2:
            # Start from head
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            # Start from tail
            current = self.tail
            for _ in range(self._size - 1 - index):
                current = current.prev
        
        return current.value
    
    def __setitem__(self, index: int, value: T) -> None:
        """
        Set the item at the specified index.
        
        Args:
            index: The index of the item to set
            value: The new value
            
        Raises:
            IndexError: If the index is out of range
        """
        if index < 0:
            index = self._size + index
        
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        # Determine whether to start from head or tail based on which is closer
        if index < self._size // 2:
            # Start from head
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            # Start from tail
            current = self.tail
            for _ in range(self._size - 1 - index):
                current = current.prev
        
        current.value = value
    
    def __str__(self) -> str:
        """Return a string representation of the list."""
        return str(list(self))
    
    def __repr__(self) -> str:
        """Return a string representation of the list."""
        return f"DoublyLinkedList({list(self)})"
    
    def __eq__(self, other: Any) -> bool:
        """
        Check if this list equals another object.
        
        Args:
            other: The object to compare with
            
        Returns:
            True if the lists are equal, False otherwise
        """
        if isinstance(other, DoublyLinkedList):
            return list(self) == list(other)
        elif isinstance(other, list):
            return list(self) == other
        return False
    
    def append(self, value: T) -> None:
        """
        Append a value to the end of the list.
        
        Args:
            value: The value to append
        """
        new_node = Node(value)
        
        if not self.head:
            # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            # List is not empty
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: T) -> None:
        """
        Prepend a value to the beginning of the list.
        
        Args:
            value: The value to prepend
        """
        new_node = Node(value)
        
        if not self.head:
            # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            # List is not empty
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self._size += 1
    
    def insert(self, index: int, value: T) -> None:
        """
        Insert a value at the specified index.
        
        Args:
            index: The index to insert at
            value: The value to insert
            
        Raises:
            IndexError: If the index is out of range
        """
        if index < 0:
            index = self._size + index
        
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(value)
        elif index == self._size:
            self.append(value)
        else:
            # Find the node at index
            current = self.head
            for _ in range(index):
                current = current.next
            
            # Create new node and insert it before current
            new_node = Node(value)
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            
            self._size += 1
    
    def remove(self, value: T) -> None:
        """
        Remove the first occurrence of a value from the list.
        
        Args:
            value: The value to remove
            
        Raises:
            ValueError: If the value is not found
        """
        current = self.head
        
        while current:
            if current.value == value:
                self._remove_node(current)
                return
            current = current.next
        
        raise ValueError(f"Value {value} not found in list")
    
    def pop(self, index: int = -1) -> T:
        """
        Remove and return the item at the specified index.
        
        Args:
            index: The index of the item to remove (default: -1, the last item)
            
        Returns:
            The value that was removed
            
        Raises:
            IndexError: If the index is out of range
        """
        if self._size == 0:
            raise IndexError("Pop from empty list")
        
        if index < 0:
            index = self._size + index
        
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        # Find the node at index
        if index == 0:
            # Remove head
            value = self.head.value
            self._remove_node(self.head)
            return value
        elif index == self._size - 1:
            # Remove tail
            value = self.tail.value
            self._remove_node(self.tail)
            return value
        else:
            # Remove node at index
            current = self.head
            for _ in range(index):
                current = current.next
            
            value = current.value
            self._remove_node(current)
            return value
    
    def _remove_node(self, node: Node[T]) -> None:
        """
        Remove a node from the list.
        
        Args:
            node: The node to remove
        """
        if node is self.head and node is self.tail:
            # Removing the only node
            self.head = None
            self.tail = None
        elif node is self.head:
            # Removing the head
            self.head = node.next
            self.head.prev = None
        elif node is self.tail:
            # Removing the tail
            self.tail = node.prev
            self.tail.next = None
        else:
            # Removing a middle node
            node.prev.next = node.next
            node.next.prev = node.prev
        
        self._size -= 1
    
    def index(self, value: T) -> int:
        """
        Return the index of the first occurrence of a value.
        
        Args:
            value: The value to find
            
        Returns:
            The index of the value
            
        Raises:
            ValueError: If the value is not found
        """
        current = self.head
        index = 0
        
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        
        raise ValueError(f"Value {value} not found in list")
    
    def clear(self) -> None:
        """Clear the list."""
        self.head = None
        self.tail = None
        self._size = 0
    
    def copy(self) -> 'DoublyLinkedList[T]':
        """
        Return a shallow copy of the list.
        
        Returns:
            A new DoublyLinkedList with the same values
        """
        return DoublyLinkedList(list(self))
    
    def swap(self, i: int, j: int) -> None:
        """
        Swap the values at indices i and j.
        
        This is more efficient than swapping the nodes themselves.
        
        Args:
            i: The first index
            j: The second index
            
        Raises:
            IndexError: If either index is out of range
        """
        if i == j:
            return
        
        if i < 0:
            i = self._size + i
        if j < 0:
            j = self._size + j
        
        if (i < 0 or i >= self._size) or (j < 0 or j >= self._size):
            raise IndexError("Index out of range")
        
        # Get nodes at indices i and j
        node_i = self._get_node(i)
        node_j = self._get_node(j)
        
        # Swap values
        node_i.value, node_j.value = node_j.value, node_i.value
    
    def _get_node(self, index: int) -> Node[T]:
        """
        Get the node at the specified index.
        
        Args:
            index: The index of the node to get
            
        Returns:
            The node at the specified index
            
        Raises:
            IndexError: If the index is out of range
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        # Determine whether to start from head or tail based on which is closer
        if index < self._size // 2:
            # Start from head
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            # Start from tail
            current = self.tail
            for _ in range(self._size - 1 - index):
                current = current.prev
        
        return current
    
    def to_list(self) -> List[T]:
        """
        Convert the linked list to a Python list.
        
        Returns:
            A list containing all values in the linked list
        """
        return list(self)
    
    @classmethod
    def from_list(cls, lst: List[T]) -> 'DoublyLinkedList[T]':
        """
        Create a new DoublyLinkedList from a Python list.
        
        Args:
            lst: The list to convert
            
        Returns:
            A new DoublyLinkedList containing the values from the list
        """
        return cls(lst)


# Adapter functions for sorting algorithms to work with DoublyLinkedList

def adapt_sort_algorithm(sort_func: Callable) -> Callable:
    """
    Adapt a sorting algorithm to work with DoublyLinkedList.
    
    This decorator converts a sorting function that works with lists to one that
    works with DoublyLinkedList instances.
    
    Args:
        sort_func: The sorting function to adapt
        
    Returns:
        An adapted version of the function that works with DoublyLinkedList
    """
    @functools.wraps(sort_func)
    def wrapper(data: Union[List[int], DoublyLinkedList[int]], trace: bool = False) -> Union[
        DoublyLinkedList[int], Generator[DoublyLinkedList[int], None, DoublyLinkedList[int]]
    ]:
        is_linked_list = isinstance(data, DoublyLinkedList)
        
        # If it's a linked list, convert to a regular list
        if is_linked_list:
            regular_list = data.to_list()
        else:
            regular_list = data
            
        # Run the original sort function
        if trace:
            # Get the generator from the original function
            result_gen = sort_func(regular_list, trace=True)
            
            # Yield results as DoublyLinkedList if input was DoublyLinkedList
            if is_linked_list:
                for state in result_gen:
                    yield DoublyLinkedList(state)
                return DoublyLinkedList(list(regular_list))  # Final state
            else:
                return result_gen  # Pass through the original generator
        else:
            # Get the sorted list from the original function
            sorted_list = sort_func(regular_list)
            
            # Convert back to DoublyLinkedList if input was DoublyLinkedList
            if is_linked_list:
                return DoublyLinkedList(sorted_list)
            else:
                return sorted_list
                
    return wrapper


# Dictionary to store adapted versions of sorting algorithms
LINKED_LIST_ALGORITHMS: Dict[str, Callable] = {}


def register_linked_list_algorithm(name: str, algorithm: Callable) -> None:
    """
    Register a sorting algorithm for use with DoublyLinkedList.
    
    Args:
        name: The name of the algorithm
        algorithm: The algorithm function to register
    """
    LINKED_LIST_ALGORITHMS[name] = adapt_sort_algorithm(algorithm)


def get_linked_list_algorithm(name: str) -> Callable:
    """
    Get an adapted sorting algorithm by name.
    
    Args:
        name: The name of the sorting algorithm
        
    Returns:
        The adapted sorting function
        
    Raises:
        ValueError: If the algorithm name is not recognized
    """
    if name not in LINKED_LIST_ALGORITHMS:
        valid_names = list(LINKED_LIST_ALGORITHMS.keys())
        raise ValueError(f"Unknown algorithm: {name}. Valid options are: {valid_names}")
    
    return LINKED_LIST_ALGORITHMS[name]


def list_linked_list_algorithms() -> List[str]:
    """
    List all available linked list sorting algorithms.
    
    Returns:
        A list of all available algorithm names
    """
    return list(LINKED_LIST_ALGORITHMS.keys())
