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
def insertion_sort(data: List[int], trace: bool = False) -> List[int]:
    """
    Implementation of Insertion Sort algorithm.
    
    Insertion sort builds the final sorted array one item at a time. 
    It takes each element from the unsorted part and inserts it into its 
    correct position in the sorted part.
    
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
    if trace and hasattr(insertion_sort, 'is_traceable'):
        return _insertion_sort_trace(arr)
    
    # The normal non-tracing version
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Place the key at its correct position
        arr[j + 1] = key
    
    return arr


def _insertion_sort_trace(data: List[int]) -> Generator[List[int], None, List[int]]:
    """
    Generator version of insertion sort that yields after each insertion.
    
    Args:
        data: The list to be sorted
        
    Yields:
        The list at each step of the sorting process
    
    Returns:
        The final sorted list
    """
    arr = data  # The caller already made a copy
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Initial state before inserting the current element
        initial_state = copy.deepcopy(arr)
        
        # Move elements greater than key one position ahead
        moved = False
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            moved = True
            
        # Place the key at its correct position
        arr[j + 1] = key
        
        # Only yield if we actually moved elements
        if moved or arr[i] != initial_state[i]:
            yield copy.deepcopy(arr)
    
    return arr

# Add an attribute to indicate this function yields a generator when trace=True
insertion_sort.is_generator = True
