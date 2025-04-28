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

from typing import Protocol, TypeVar, List, Generator, Callable, Any, Union, cast, overload
import functools
import copy

T = TypeVar('T')


class SortAlgorithm(Protocol):
    """Protocol defining the interface for all sorting algorithms."""
    
    def __call__(
        self, data: List[int], trace: bool = False
    ) -> Union[List[int], Generator[List[int], None, List[int]]]:
        """
        Sort the input list.
        
        Args:
            data: The list to be sorted
            trace: If True, yield intermediate states during sorting
                  If False, just return the final sorted list
                  
        Returns:
            If trace is False, return the sorted list
            If trace is True, yield a generator of intermediate states,
            with the final state being the sorted list
        """
        ...


def traceable(func: Callable) -> Callable:
    """
    Decorator that adds tracing capability to sorting functions.
    
    When trace=True, the decorated function will yield intermediate states
    as the sorting algorithm progresses.
    
    When trace=False, the decorated function will simply return the
    final sorted list.
    
    Args:
        func: The sorting function to decorate
        
    Returns:
        A wrapped function that can either return a sorted list or
        yield intermediate states
    """
    @functools.wraps(func)
    def wrapper(data: List[int], trace: bool = False) -> Union[List[int], Generator[List[int], None, List[int]]]:
        # Make a copy of the input data to avoid modifying the original
        data_copy = copy.deepcopy(data)
        
        if not trace:
            # If tracing is disabled, just call the original function
            return func(data_copy)
        
        # If tracing is enabled, wrap the function to yield intermediate states
        def trace_generator() -> Generator[List[int], None, List[int]]:
            # Yield the initial state
            yield copy.deepcopy(data_copy)
            
            # For functions that return a generator when tracing is enabled
            if hasattr(func, 'is_generator'):
                # Pass along all intermediate states from the function
                for state in func(data_copy, trace=True):
                    yield copy.deepcopy(state)
            else:
                # For functions that don't yield intermediate states,
                # just call the function and yield the final result
                result = func(data_copy)
                yield copy.deepcopy(result)
                return result
                
        return trace_generator()
    
    # Add a flag to indicate this function has been decorated
    wrapper.is_traceable = True
    
    return wrapper
