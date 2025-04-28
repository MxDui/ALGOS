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

# Expose all sorting algorithms
from sortkit.core.selection import selection_sort
from sortkit.core.insertion import insertion_sort
from sortkit.core.quick import quick_sort
from sortkit.core.merge import merge_sort
from sortkit.core.heap import heap_sort

# Expose registry
from sortkit.registry import ALGORITHMS, get_algorithm, list_algorithms

__version__ = "1.0.0"
