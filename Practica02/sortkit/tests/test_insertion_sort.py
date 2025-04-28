 

import pytest
from typing import List

from sortkit.core.insertion import insertion_sort
from sortkit.structs.dllist import DoublyLinkedList


class TestInsertionSort:
    """Test suite for insertion sort algorithm."""

    def test_empty_list(self, empty_list: List[int]):
        """Test sorting an empty list."""
        result = insertion_sort(empty_list)
        assert result == []

    def test_single_element_list(self, single_element_list: List[int]):
        """Test sorting a single element list."""
        result = insertion_sort(single_element_list)
        assert result == [42]

    def test_sorted_list(self, sorted_list: List[int]):
        """Test sorting an already sorted list."""
        result = insertion_sort(sorted_list)
        assert result == sorted_list

    def test_reversed_list(self, reversed_list: List[int]):
        """Test sorting a reversed list."""
        result = insertion_sort(reversed_list)
        assert result == sorted(reversed_list)

    def test_random_list(self, random_list: List[int]):
        """Test sorting a random list."""
        result = insertion_sort(random_list)
        assert result == sorted(random_list)

    def test_duplicates_list(self, duplicates_list: List[int]):
        """Test sorting a list with duplicates."""
        result = insertion_sort(duplicates_list)
        assert result == sorted(duplicates_list)

    def test_large_list(self):
        """Test sorting a large list."""
        import random
        large_list = [random.randint(0, 1000) for _ in range(500)]  # Smaller size for insertion sort as it's O(n²)
        result = insertion_sort(large_list)
        assert result == sorted(large_list)

    def test_stability(self):
        """Test that insertion sort is stable (maintains relative order of equal elements)."""
        # Create a list of objects with custom comparison logic
        class Record:
            def __init__(self, key, value):
                self.key = key
                self.value = value
            
            def __lt__(self, other):
                return self.key < other.key
            
            def __eq__(self, other):
                return self.key == other.key and self.value == other.value
                
            def __repr__(self):
                return f"Record({self.key}, {self.value})"
                
        # Create test data with duplicates
        original_list = [
            Record(5, 1), Record(3, 2), Record(5, 3), Record(2, 4), Record(3, 5)
        ]
        
        # Sort the list
        result = insertion_sort(original_list)
        
        # Extract the keys and values
        sorted_keys = [record.key for record in result]
        
        # Check that the list is sorted by keys
        for i in range(len(sorted_keys) - 1):
            assert sorted_keys[i] <= sorted_keys[i + 1]
        
        # Check stability: equal keys should maintain their original relative order
        # Find the positions of records with key 5
        key_5_values = [r.value for r in result if r.key == 5]
        assert key_5_values == [1, 3]  # The original order was (5,1) then (5,3)
        
        # Find the positions of records with key 3
        key_3_values = [r.value for r in result if r.key == 3]
        assert key_3_values == [2, 5]  # The original order was (3,2) then (3,5) 