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

from typing import Dict, Callable, List, Union, Generator
from sortkit.core.selection import selection_sort
from sortkit.core.insertion import insertion_sort
from sortkit.core.quick import quick_sort
from sortkit.core.merge import merge_sort
from sortkit.core.heap import heap_sort


# Dictionary mapping algorithm names to their implementations
ALGORITHMS: Dict[str, Callable] = {
    "selection": selection_sort,
    "insertion": insertion_sort,
    "quick": quick_sort,
    "merge": merge_sort,
    "heap": heap_sort,
}


def get_algorithm(name: str) -> Callable:
    """
    Get a sorting algorithm by name.
    
    Args:
        name: The name of the sorting algorithm
        
    Returns:
        The corresponding sorting function
        
    Raises:
        ValueError: If the algorithm name is not recognized
    """
    if name not in ALGORITHMS:
        valid_names = list(ALGORITHMS.keys())
        raise ValueError(f"Unknown algorithm: {name}. Valid options are: {valid_names}")
    
    return ALGORITHMS[name]


def list_algorithms() -> List[str]:
    """
    List all available sorting algorithms.
    
    Returns:
        A list of all available algorithm names
    """
    return list(ALGORITHMS.keys())
