 

import pytest
from typing import List

from sortkit.core.merge import merge_sort
from sortkit.structs.dllist import DoublyLinkedList


class TestMergeSort:
    """Test suite for merge sort algorithm."""

    def test_empty_list(self, empty_list: List[int]):
        """Test sorting an empty list."""
        result = merge_sort(empty_list)
        assert result == []

    def test_single_element_list(self, single_element_list: List[int]):
        """Test sorting a single element list."""
        result = merge_sort(single_element_list)
        assert result == [42]

    def test_sorted_list(self, sorted_list: List[int]):
        """Test sorting an already sorted list."""
        result = merge_sort(sorted_list)
        assert result == sorted_list

    def test_reversed_list(self, reversed_list: List[int]):
        """Test sorting a reversed list."""
        result = merge_sort(reversed_list)
        assert result == sorted(reversed_list)

    def test_random_list(self, random_list: List[int]):
        """Test sorting a random list."""
        result = merge_sort(random_list)
        assert result == sorted(random_list)

    def test_duplicates_list(self, duplicates_list: List[int]):
        """Test sorting a list with duplicates."""
        result = merge_sort(duplicates_list)
        assert result == sorted(duplicates_list)

    def test_large_list(self):
        """Test sorting a large list."""
        import random
        large_list = [random.randint(0, 1000) for _ in range(1000)]
        result = merge_sort(large_list)
        assert result == sorted(large_list)

    def test_stability(self):
        """Test that merge sort is stable (maintains relative order of equal elements)."""
        # Create a list of tuples (value, original_position)
        original_list = [(5, 1), (3, 2), (5, 3), (2, 4), (3, 5)]
        
        # Sort by the first element in each tuple
        result = merge_sort(original_list, key=lambda x: x[0])
        
        # Check that elements are sorted by their first element
        for i in range(len(result) - 1):
            assert result[i][0] <= result[i + 1][0]
        
        # Check stability: equal elements should maintain their original order
        # For the value 5, original positions were 1, 3
        five_positions = [item[1] for item in result if item[0] == 5]
        assert five_positions == [1, 3]
        
        # For the value 3, original positions were 2, 5
        three_positions = [item[1] for item in result if item[0] == 3]
        assert three_positions == [2, 5] 