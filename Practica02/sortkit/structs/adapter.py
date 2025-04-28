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

from typing import Dict, List, Any, Callable, Optional
import importlib

from sortkit.algorithms.registry import get_algorithm, list_algorithms
from sortkit.structs.dllist import register_linked_list_algorithm


def register_all_for_linked_list() -> List[str]:
    """
    Register all available sorting algorithms for use with DoublyLinkedList.
    
    This function imports all registered sorting algorithms and adapts them
    for use with DoublyLinkedList.
    
    Returns:
        A list of algorithm names that were registered
    """
    registered = []
    
    # Get all available algorithms
    algorithms = list_algorithms()
    
    # Register each algorithm for use with DoublyLinkedList
    for name in algorithms:
        algorithm = get_algorithm(name)
        register_linked_list_algorithm(name, algorithm)
        registered.append(name)
    
    return registered 