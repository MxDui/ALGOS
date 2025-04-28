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

from typing import List, Generator, Union
import copy
from sortkit.core.base import traceable


@traceable
def heap_sort(data: List[int], trace: bool = False) -> List[int]:
    """
    Implementation of Heap Sort algorithm.
    
    Heap sort builds a max heap from the array and repeatedly extracts
    the maximum element, placing it at the end of the array.
    
    Args:
        data: The list to be sorted
        trace: If True, the original function will be wrapped to yield 
               intermediate states. This parameter is used by the traceable decorator.
    
    Returns:
        The sorted list
    """
    # Make a working copy to avoid modifying the input
    arr = copy.deepcopy(data)
    
    # This is the generator version called by the traceable decorator
    if trace and hasattr(heap_sort, 'is_traceable'):
        return _heap_sort_trace(arr)
    
    # The normal non-tracing version
    n = len(arr)
    
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        _heapify(arr, i, 0)
    
    return arr


def _heapify(arr: List[int], n: int, i: int) -> None:
    """
    Heapify a subtree rooted at index i.
    
    Args:
        arr: The array to heapify
        n: The size of the heap
        i: The index of the root of the subtree to heapify
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child
    
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If the largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        
        # Recursively heapify the affected subtree
        _heapify(arr, n, largest)


def _heap_sort_trace(arr: List[int]) -> Generator[List[int], None, List[int]]:
    """
    Generator version of heap sort that yields after each significant step.
    
    Args:
        arr: The list to be sorted
        
    Yields:
        The list at each step of the sorting process
    
    Returns:
        The final sorted list
    """
    n = len(arr)
    
    # Build a max heap and yield after construction
    for i in range(n // 2 - 1, -1, -1):
        _heapify_trace(arr, n, i)
    
    yield copy.deepcopy(arr)  # Yield after max heap is built
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        _heapify_trace(arr, i, 0)
        yield copy.deepcopy(arr)  # Yield after each extraction
    
    return arr


def _heapify_trace(arr: List[int], n: int, i: int) -> None:
    """
    Trace-enabled version of the heapify function.
    Identical to _heapify but used for tracing.
    
    Args:
        arr: The array to heapify
        n: The size of the heap
        i: The index of the root of the subtree to heapify
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child
    
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If the largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        
        # Recursively heapify the affected subtree
        _heapify_trace(arr, n, largest)

# Add an attribute to indicate this function yields a generator when trace=True
heap_sort.is_generator = True
