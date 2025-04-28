# Expose all sorting algorithms
from practica02.core.selection import selection_sort
from practica02.core.insertion import insertion_sort
from practica02.core.quick import quick_sort
from practica02.core.merge import merge_sort
from practica02.core.heap import heap_sort

# Expose registry
from practica02.registry import ALGORITHMS, get_algorithm, list_algorithms

__version__ = "1.0.0" 