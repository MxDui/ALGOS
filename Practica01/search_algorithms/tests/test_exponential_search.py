import unittest
from search_algorithms.algorithms import ExponentialSearch

class TestExponentialSearch(unittest.TestCase):
    
    def setUp(self):
        self.search = ExponentialSearch()
    
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
        
    def test_large_array(self):
        """Test with a large array to verify exponential behavior"""
        arr = [i for i in range(100)]
        
        # Element in the first half
        result = self.search.search(arr, 30)
        self.assertEqual(result, 30)
        
        # Element in the second half
        result = self.search.search(arr, 80)
        self.assertEqual(result, 80)
        
    def test_array_with_duplicates(self):
        """Test search with duplicates"""
        arr = [1, 2, 2, 2, 3, 4, 5]
        result = self.search.search(arr, 2)
        self.assertIn(result, [1, 2, 3])  # Could be any of these positions
        
    def test_iteration_efficiency(self):
        """Test the efficiency of exponential search"""
        # Create a large sorted array
        arr = [i for i in range(1024)]  # 2^10
        
        # Element at the end
        self.search.search(arr, 1000)
        
        # For exponential search, the number of iterations should be
        # significantly less than linear search would require (1000)
        self.assertLess(self.search.iterations, 50)

if __name__ == '__main__':
    unittest.main() 