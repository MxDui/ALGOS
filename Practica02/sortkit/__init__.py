 

# Expose all sorting algorithms
from sortkit.core.selection import selection_sort
from sortkit.core.insertion import insertion_sort
from sortkit.core.quick import quick_sort
from sortkit.core.merge import merge_sort
from sortkit.core.heap import heap_sort

# Expose registry
from sortkit.registry import ALGORITHMS, get_algorithm, list_algorithms

__version__ = "1.0.0"
