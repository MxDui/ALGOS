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

from typing import List, Generator, Union, Tuple
import copy
from sortkit.core.base import traceable


@traceable
def quick_sort(data: List[int], trace: bool = False) -> List[int]:
    """
    Implementation of Quick Sort algorithm.
    
    Quick sort selects a 'pivot' element and partitions the array around it
    so that elements less than the pivot are on the left and elements greater
    than the pivot are on the right.
    
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
    if trace and hasattr(quick_sort, 'is_traceable'):
        return _quick_sort_trace(arr, 0, len(arr) - 1)
    
    # The normal non-tracing version
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr: List[int], low: int, high: int) -> None:
    """
    Helper function for the recursive quicksort algorithm.
    
    Args:
        arr: The list to be sorted (in-place)
        low: The starting index of the subarray to sort
        high: The ending index of the subarray to sort
    """
    if low < high:
        # Partition array and get pivot index
        pivot_idx = _partition(arr, low, high)
        
        # Recursively sort the subarrays
        _quick_sort(arr, low, pivot_idx - 1)
        _quick_sort(arr, pivot_idx + 1, high)


def _partition(arr: List[int], low: int, high: int) -> int:
    """
    Partition the array around a pivot.
    
    Args:
        arr: The list to partition (in-place)
        low: The starting index of the subarray to partition
        high: The ending index of the subarray to partition
        
    Returns:
        The index of the pivot after partitioning
    """
    # Choose the rightmost element as the pivot
    pivot = arr[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place the pivot in its final position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _quick_sort_trace(arr: List[int], low: int, high: int) -> Generator[List[int], None, List[int]]:
    """
    Generator version of quicksort that yields after each partition.
    
    Args:
        arr: The list to be sorted
        low: The starting index of the subarray to sort
        high: The ending index of the subarray to sort
        
    Yields:
        The list at each step of the partitioning process
    
    Returns:
        The final sorted list
    """
    if low < high:
        # Partition array and get pivot index
        pivot_idx = _partition_trace(arr, low, high)
        yield copy.deepcopy(arr)
        
        # Recursively sort the subarrays and yield results
        yield from _quick_sort_trace(arr, low, pivot_idx - 1)
        yield from _quick_sort_trace(arr, pivot_idx + 1, high)
    
    return arr


def _partition_trace(arr: List[int], low: int, high: int) -> int:
    """
    Trace-enabled version of the partition function.
    Identical to _partition but used for tracing.
    
    Args:
        arr: The list to partition (in-place)
        low: The starting index of the subarray to partition
        high: The ending index of the subarray to partition
        
    Returns:
        The index of the pivot after partitioning
    """
    # Choose the rightmost element as the pivot
    pivot = arr[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place the pivot in its final position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Add an attribute to indicate this function yields a generator when trace=True
quick_sort.is_generator = True
