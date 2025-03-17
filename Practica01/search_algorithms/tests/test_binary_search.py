import unittest
from search_algorithms.algorithms import BinarySearch

class TestBinarySearch(unittest.TestCase):
    
    def setUp(self):
        self.search = BinarySearch()
    
    def test_empty_array(self):
        """Test searching in an empty array"""
        result = self.search.search([], 5)
        self.assertEqual(result, -1)
        
    def test_element_at_beginning(self):
        """Test finding an element at the beginning of the array"""
        arr = [1, 2, 3, 4, 5]
        result = self.search.search(arr, 1)
        self.assertEqual(result, 0)
        
    def test_element_at_middle(self):
        """Test finding an element in the middle of the array"""
        arr = [1, 2, 3, 4, 5]
        result = self.search.search(arr, 3)
        self.assertEqual(result, 2)
        
    def test_element_at_end(self):
        """Test finding an element at the end of the array"""
        arr = [1, 2, 3, 4, 5]
        result = self.search.search(arr, 5)
        self.assertEqual(result, 4)
        
    def test_element_not_in_array(self):
        """Test searching for an element not in the array"""
        arr = [1, 2, 3, 4, 5]
        result = self.search.search(arr, 6)
        self.assertEqual(result, -1)
        
    def test_array_with_one_element(self):
        """Test searching in an array with one element"""
        arr = [5]
        result = self.search.search(arr, 5)
        self.assertEqual(result, 0)
        
        result = self.search.search(arr, 1)
        self.assertEqual(result, -1)
        
    def test_array_with_duplicates(self):
        """Test search with duplicates - should find any occurrence"""
        arr = [1, 2, 2, 2, 3, 4, 5]
        result = self.search.search(arr, 2)
        self.assertIn(result, [1, 2, 3])  # Could be any of these positions
        
    def test_iteration_count(self):
        """Test the iteration counter for binary search"""
        # Test with array of size 16 (2^4)
        arr = [i for i in range(16)]
        
        # Element in the middle
        self.search.search(arr, 8)
        self.assertLessEqual(self.search.iterations, 4)  # log2(16) = 4
        
        # Worst case (element not in array)
        self.search.search(arr, 20)
        self.assertLessEqual(self.search.iterations, 5)  # log2(16) + 1 = 5
        
    def test_search_range(self):
        """Test the search_range method"""
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        # Search in a subrange
        result = self.search.search_range(arr, 4, 2, 6, 0)
        self.assertEqual(result, 3)
        
        # Element outside the specified range
        result = self.search.search_range(arr, 9, 0, 5, 0)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main() 