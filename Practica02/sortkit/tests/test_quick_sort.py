 

import pytest
from typing import List

from sortkit.core.quick import quick_sort
from sortkit.structs.dllist import DoublyLinkedList


class TestQuickSort:
    """Test suite for quick sort algorithm."""

    def test_empty_list(self, empty_list: List[int]):
        """Test sorting an empty list."""
        result = quick_sort(empty_list)
        assert result == []

    def test_single_element_list(self, single_element_list: List[int]):
        """Test sorting a single element list."""
        result = quick_sort(single_element_list)
        assert result == [42]

    def test_sorted_list(self, sorted_list: List[int]):
        """Test sorting an already sorted list."""
        result = quick_sort(sorted_list)
        assert result == sorted_list

    def test_reversed_list(self, reversed_list: List[int]):
        """Test sorting a reversed list."""
        result = quick_sort(reversed_list)
        assert result == sorted(reversed_list)

    def test_random_list(self, random_list: List[int]):
        """Test sorting a random list."""
        result = quick_sort(random_list)
        assert result == sorted(random_list)

    def test_duplicates_list(self, duplicates_list: List[int]):
        """Test sorting a list with duplicates."""
        result = quick_sort(duplicates_list)
        assert result == sorted(duplicates_list)

    def test_large_list(self):
        """Test sorting a large list."""
        import random
        large_list = [random.randint(0, 1000) for _ in range(1000)]
        result = quick_sort(large_list)
        assert result == sorted(large_list)

    def test_fixed_pivot(self):
        """Test sorting with a fixed pivot selection strategy."""
        test_list = [5, 3, 8, 4, 2, 1, 9, 7]
        result = quick_sort(test_list, pivot_strategy="first")
        assert result == sorted(test_list)
        
        result = quick_sort(test_list, pivot_strategy="last")
        assert result == sorted(test_list)
        
        result = quick_sort(test_list, pivot_strategy="middle")
        assert result == sorted(test_list)
        
        result = quick_sort(test_list, pivot_strategy="random")
        assert result == sorted(test_list)
    
    def test_stability(self):
        """Test that quick sort is NOT stable (doesn't maintain relative order of equal elements)."""
        # Create a list of tuples (value, original_position)
        original_list = [(5, 1), (3, 2), (5, 3), (2, 4), (3, 5)]
        
        # Sort by the first element in each tuple
        result = quick_sort(original_list, key=lambda x: x[0])
        
        # Check that elements are sorted by their first element
        for i in range(len(result) - 1):
            assert result[i][0] <= result[i + 1][0]
        
        # Quick sort is NOT stable, so we can't make specific assertions about
        # the ordering of equal elements, we just verify the list is sorted correctly
        assert sorted(result, key=lambda x: x[0]) == result 