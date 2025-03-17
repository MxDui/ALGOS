import unittest
import random
from search_algorithms.algorithms import SearchAlgorithmFactory
from search_algorithms.utils import measure_time, run_performance_test

class TestPerformance(unittest.TestCase):
    
    def setUp(self):
        # Get all search algorithms
        self.algorithms = SearchAlgorithmFactory.get_all_algorithms()
        
        # Create sample arrays of different sizes
        self.small_array = list(range(100))
        self.medium_array = list(range(1000))
        self.large_array = list(range(10000))
        
        # Shuffle copies for testing linear search with unsorted arrays
        self.small_unsorted = self.small_array.copy()
        random.shuffle(self.small_unsorted)
        
    def test_measure_time(self):
        """Test the measure_time function"""
        # Choose an algorithm
        binary_search = self.algorithms["binary"]
        
        # Measure time for a simple search
        time_taken = measure_time(binary_search, self.small_array, 50, repetitions=10)
        
        # Time should be a positive number
        self.assertGreater(time_taken, 0)
        
        # For a small array, search should be very fast (< 0.001 seconds typically)
        # This is a rough check; exact time will vary by system
        self.assertLess(time_taken, 0.001)
        
    def test_algorithm_efficiency_comparison(self):
        """Compare efficiency of different algorithms"""
        # We'll use the medium array and search for an element near the end
        target = self.medium_array[900]  # Element near the end
        
        # Measure time for each algorithm
        times = {}
        for name, algorithm in self.algorithms.items():
            # Skip interpolation search for string arrays
            times[name] = measure_time(algorithm, self.medium_array, target, repetitions=10)
            
        # Binary, interpolation, and exponential should be faster than linear for sorted arrays
        self.assertLess(times["binary"], times["linear"])
        self.assertLess(times["exponential"], times["linear"])
        
        # These are approximate relationships that should generally hold
        # for searching in sorted arrays, but may vary by implementation
        self.assertLessEqual(times["binary"] * 2, times["linear"])
        
    def test_run_performance_test(self):
        """Test the run_performance_test function"""
        # Run a small performance test
        sizes = [10, 100]
        results = run_performance_test(
            self.algorithms,
            sizes=sizes,
            repetitions=5,
            position='end'  # Search for elements at the end (worst case for many algorithms)
        )
        
        # Check that results contain expected algorithm names
        for algo_name in self.algorithms.keys():
            self.assertIn(algo_name, results)
        
        # Check that sizes were recorded correctly
        self.assertIn('sizes', results)
        self.assertEqual(results['sizes'], sizes)
        
        # Check that each algorithm has results for each array size
        for algo_name in self.algorithms.keys():
            # Check results structure
            self.assertIn('times', results[algo_name])
            self.assertIn('iterations', results[algo_name])
            
            # Check if 'times' and 'iterations' lists have the correct length
            self.assertEqual(len(results[algo_name]['times']), len(sizes))
            self.assertEqual(len(results[algo_name]['iterations']), len(sizes))
            
        # Binary search should have fewer iterations than linear search for larger arrays
        # (index 1 is for the size 100 array)
        self.assertLess(
            results['binary']['iterations'][1],  # Binary search iterations for size 100
            results['linear']['iterations'][1]   # Linear search iterations for size 100
        )
        
    def test_linear_search_with_unsorted_array(self):
        """Test that linear search works with unsorted arrays"""
        linear = self.algorithms["linear"]
        
        # Pick a value we know is in the array
        value = self.small_unsorted[20]
        
        # Search should find the value
        index = linear.search(self.small_unsorted, value)
        self.assertNotEqual(index, -1)
        self.assertEqual(self.small_unsorted[index], value)

if __name__ == '__main__':
    unittest.main() 