from typing import List, Generator, Union
import copy


def selection_sort(data: List[int], trace: bool = False) -> Union[List[int], Generator[List[int], None, None]]:
    """
    Implementation of Selection Sort algorithm.
    
    Selection sort works by finding the minimum element from the unsorted part
    of the array and putting it at the beginning of the unsorted part.
    
    Args:
        data: The list to be sorted
        trace: If True, yield intermediate states during sorting
        
    Returns:
        If trace is False: The sorted list
        If trace is True: A generator yielding steps of the sorting process
    """
    # Make a working copy to avoid modifying the input
    arr = copy.deepcopy(data)
    
    if trace:
        return _selection_sort_with_trace(arr)
    else:
        return _selection_sort_without_trace(arr)


def _selection_sort_without_trace(arr: List[int]) -> List[int]:
    """
    Standard implementation of selection sort.
    
    Args:
        arr: The list to be sorted
        
    Returns:
        The sorted list
    """
    n = len(arr)
    
    for i in range(n - 1):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def _selection_sort_with_trace(arr: List[int]) -> Generator[List[int], None, None]:
    """
    Selection sort with tracing that yields after each swap.
    
    Args:
        arr: The list to be sorted
        
    Yields:
        The list at each step of the sorting process
    """
    n = len(arr)
    
    # Yield the initial state
    yield copy.deepcopy(arr)
    
    for i in range(n - 1):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        if min_idx != i:  # Only swap if needed
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            yield copy.deepcopy(arr)
    
    # The generator will be consumed by the calling function 