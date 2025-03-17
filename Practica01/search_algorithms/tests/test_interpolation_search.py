import unittest
from search_algorithms.algorithms import InterpolationSearch

class TestInterpolationSearch(unittest.TestCase):
    
    def setUp(self):
        self.search = InterpolationSearch()
    
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
        
    def test_uniform_distribution(self):
        """Test with uniformly distributed array (best case for interpolation)"""
        arr = [i for i in range(0, 100, 2)]  # Evenly spaced elements
        
        # Find element at position 25 (value 50)
        result = self.search.search(arr, 50)
        self.assertEqual(result, 25)
        
        # Check that it's efficient (should find quickly in uniform array)
        self.search.search(arr, 50)
        self.assertLessEqual(self.search.iterations, 4)
        
    def test_non_uniform_distribution(self):
        """Test with non-uniform distribution"""
        # Exponentially growing values
        arr = [2**i for i in range(10)]  # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        
        # Find different elements
        result = self.search.search(arr, 16)
        self.assertEqual(result, 4)
        
        result = self.search.search(arr, 512)
        self.assertEqual(result, 9)
        
    def test_string_array(self):
        """Test with string elements"""
        arr = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
        
        result = self.search.search(arr, "cherry")
        self.assertEqual(result, 2)
        
        result = self.search.search(arr, "grape")
        self.assertEqual(result, -1)
        
    def test_duplicate_elements(self):
        """Test search with duplicates"""
        arr = [1, 2, 2, 2, 3, 4, 5]
        result = self.search.search(arr, 2)
        self.assertIn(result, [1, 2, 3])  # Could be any of these positions

if __name__ == '__main__':
    unittest.main() 