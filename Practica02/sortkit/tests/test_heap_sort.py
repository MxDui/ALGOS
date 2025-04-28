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

import pytest
from typing import List

from sortkit.core.heap import heap_sort, _heapify, _build_max_heap
from sortkit.structs.dllist import DoublyLinkedList


class TestHeapSort:
    """Test suite for heap sort algorithm."""

    def test_empty_list(self, empty_list: List[int]):
        """Test sorting an empty list."""
        result = heap_sort(empty_list)
        assert result == []

    def test_single_element_list(self, single_element_list: List[int]):
        """Test sorting a single element list."""
        result = heap_sort(single_element_list)
        assert result == [42]

    def test_sorted_list(self, sorted_list: List[int]):
        """Test sorting an already sorted list."""
        result = heap_sort(sorted_list)
        assert result == sorted_list

    def test_reversed_list(self, reversed_list: List[int]):
        """Test sorting a reversed list."""
        result = heap_sort(reversed_list)
        assert result == sorted(reversed_list)

    def test_random_list(self, random_list: List[int]):
        """Test sorting a random list."""
        result = heap_sort(random_list)
        assert result == sorted(random_list)

    def test_duplicates_list(self, duplicates_list: List[int]):
        """Test sorting a list with duplicates."""
        result = heap_sort(duplicates_list)
        assert result == sorted(duplicates_list)

    def test_large_list(self):
        """Test sorting a large list."""
        import random
        large_list = [random.randint(0, 1000) for _ in range(1000)]
        result = heap_sort(large_list)
        assert result == sorted(large_list)

    def test_heapify_process(self):
        """Test the heapify process specifically."""
        # This test checks if the heap property is maintained during sorting
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        
        # Make a copy to test intermediate steps
        test_arr = arr.copy()
        
        # After building max heap, the largest element should be at the root (index 0)
        # We'll call a helper function to build the heap
        _build_max_heap(test_arr)
        assert test_arr[0] == max(arr)
        
        # Remove the root and test heap property again
        # (This simulates part of the heap sort process)
        test_arr[0], test_arr[-1] = test_arr[-1], test_arr[0]
        heap_size = len(test_arr) - 1
        _heapify(test_arr, 0, heap_size)
        
        # The new root should be the second largest element
        assert test_arr[0] == max(test_arr[:heap_size])
        
    def test_stability(self):
        """Test that heap sort is NOT stable (doesn't maintain relative order of equal elements)."""
        # Create a list of tuples (value, original_position)
        original_list = [(5, 1), (3, 2), (5, 3), (2, 4), (3, 5)]
        
        # Sort by the first element in each tuple
        result = heap_sort(original_list, key=lambda x: x[0])
        
        # Check that elements are sorted by their first element
        for i in range(len(result) - 1):
            assert result[i][0] <= result[i + 1][0]
        
        # Heap sort is NOT stable, so we can't make specific assertions about
        # the ordering of equal elements, we just verify the list is sorted correctly
        assert sorted(result, key=lambda x: x[0]) == result 