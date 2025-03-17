import unittest
from search_algorithms.algorithms import LinearSearch

class TestLinearSearch(unittest.TestCase):
    
    def setUp(self):
        self.search = LinearSearch()
    
    def test_empty_array(self):
        """Test searching in an empty array"""
        result = self.search.search([], 5)
        self.assertEqual(result, -1)
        
    def test_element_at_beginning(self):
        """Test finding an element at the beginning of the array"""
        arr = [5, 2, 4, 6, 8]
        result = self.search.search(arr, 5)
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
        
    def test_duplicate_elements(self):
        """Test finding the first occurrence of a duplicate element"""
        arr = [1, 2, 2, 3, 4, 2]
        result = self.search.search(arr, 2)
        self.assertEqual(result, 1)
        
    def test_iteration_count(self):
        """Test the iteration counter for linear search"""
        arr = [1, 2, 3, 4, 5]
        
        # Element at the beginning
        self.search.search(arr, 1)
        self.assertEqual(self.search.iterations, 1)
        
        # Element at the middle
        self.search.search(arr, 3)
        self.assertEqual(self.search.iterations, 3)
        
        # Element not in array
        self.search.search(arr, 6)
        self.assertEqual(self.search.iterations, 5)

if __name__ == '__main__':
    unittest.main() 