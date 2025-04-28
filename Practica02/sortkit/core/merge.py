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
def merge_sort(data: List[int], trace: bool = False) -> List[int]:
    """
    Implementation of Merge Sort algorithm.
    
    Merge sort divides the array into halves, sorts them recursively,
    and then merges the sorted halves.
    
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
    if trace and hasattr(merge_sort, 'is_traceable'):
        return _merge_sort_trace(arr)
    
    # The normal non-tracing version
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2
        
        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort the two halves
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)
        
        # Merge the sorted halves
        _merge(arr, left_half, right_half)
    
    return arr


def _merge(arr: List[int], left: List[int], right: List[int]) -> None:
    """
    Merge two sorted subarrays into the target array.
    
    Args:
        arr: The target array to merge into
        left: The left sorted subarray
        right: The right sorted subarray
    """
    i = j = k = 0
    
    # Merge elements from left and right into arr
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # Copy remaining elements from left (if any)
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    # Copy remaining elements from right (if any)
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def _merge_sort_trace(arr: List[int]) -> Generator[List[int], None, List[int]]:
    """
    Generator version of merge sort that yields after each merge.
    
    Args:
        arr: The list to be sorted
        
    Yields:
        The list at each step of the merging process
    
    Returns:
        The final sorted list
    """
    if len(arr) <= 1:
        return arr
    
    # Find the middle of the array
    mid = len(arr) // 2
    
    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the two halves and collect any yielded states
    left_half = list(_merge_sort_trace(left_half))[-1]  # Get the final sorted state
    right_half = list(_merge_sort_trace(right_half))[-1]  # Get the final sorted state
    
    # Merge the sorted halves and yield the result
    _merge(arr, left_half, right_half)
    yield copy.deepcopy(arr)
    
    return arr


# Add an attribute to indicate this function yields a generator when trace=True
merge_sort.is_generator = True
