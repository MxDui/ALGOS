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
def selection_sort(data: List[int], trace: bool = False) -> List[int]:
    """
    Implementation of Selection Sort algorithm.
    
    Selection sort works by finding the minimum element from the unsorted part
    of the array and putting it at the beginning of the unsorted part.
    
    Args:
        data: The list to be sorted
        trace: If True, the original function will be wrapped to yield 
               intermediate states. This parameter is used by the traceable decorator.
    
    Returns:
        The sorted list
    """
    # Make a working copy to avoid modifying the input
    arr = copy.deepcopy(data)
    n = len(arr)
    
    # This is the generator version called by the traceable decorator
    if trace and hasattr(selection_sort, 'is_traceable'):
        return _selection_sort_trace(arr)
    
    # The normal non-tracing version
    for i in range(n - 1):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def _selection_sort_trace(data: List[int]) -> Generator[List[int], None, List[int]]:
    """
    Generator version of selection sort that yields after each swap.
    
    Args:
        data: The list to be sorted
        
    Yields:
        The list at each step of the sorting process
    
    Returns:
        The final sorted list
    """
    arr = data  # The caller already made a copy
    n = len(arr)
    
    for i in range(n - 1):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        if min_idx != i:  # Only swap and yield if actually changing
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            yield copy.deepcopy(arr)
    
    return arr

# Add an attribute to indicate this function yields a generator when trace=True
selection_sort.is_generator = True
