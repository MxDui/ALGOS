import unittest
from search_algorithms.algorithms import InterpolationSearch

class TestInterpolationSearch(unittest.TestCase):
    
    def setUp(self):
        self.search = InterpolationSearch()
    
    """Test para la busqueda en arreglos vacios"""
    def test_empty_array(self):
        result = self.search.search([], 5)
        self.assertEqual(result, -1)
        
    """Test para cuando encontremos un elemento en el principio del arreglo"""
    def test_element_at_beginning(self):
        arr = [1, 2, 3, 4, 5]
        result = self.search.search(arr, 1)
        self.assertEqual(result, 0)
        
    """Test para cuando encontremos un elemento a la mitad del arreglo"""
    def test_element_at_middle(self):
        arr = [1, 2, 3, 4, 5]
        result = self.search.search(arr, 3)
        self.assertEqual(result, 2)
        
    """Test para cuando encontremos un elemento al final del arreglo"""
    def test_element_at_end(self):
        arr = [1, 2, 3, 4, 5]
        result = self.search.search(arr, 5)
        self.assertEqual(result, 4)
        
    """Test para cuando el elemento no se encuentra en el arreglo"""
    def test_element_not_in_array(self):
        arr = [1, 2, 3, 4, 5]
        result = self.search.search(arr, 6)
        self.assertEqual(result, -1)
        
    """Test para un arreglo con un elemento"""
    def test_array_with_one_element(self):
        arr = [5]
        result = self.search.search(arr, 5)
        self.assertEqual(result, 0)
        
        result = self.search.search(arr, 1)
        self.assertEqual(result, -1)
        
    """Prueba para un arreglo con distribución uniforme (el mejor caso para la interpolacion)"""
    def test_uniform_distribution(self):
        arr = [i for i in range(0, 100, 2)]  # Evenly spaced elements
        
        # Encontrar el elemento en la posiicon 25 (valor 50)
        result = self.search.search(arr, 50)
        self.assertEqual(result, 25)
        
        self.search.search(arr, 50)
        self.assertLessEqual(self.search.iterations, 4)
        
    """Prueba para un arreglo sin distribución uniforme (el peor caso para la interpolacion)"""
    def test_non_uniform_distribution(self):
        # valores con crecimiento exponencial
        arr = [2**i for i in range(10)]  # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        
        result = self.search.search(arr, 16)
        self.assertEqual(result, 4)
        
        result = self.search.search(arr, 512)
        self.assertEqual(result, 9)
        
        
    """Test para cuando hay duplicados"""
    def test_duplicate_elements(self):
        arr = [1, 2, 2, 2, 3, 4, 5]
        result = self.search.search(arr, 2)
        self.assertIn(result, [1, 2, 3])  # Could be any of these positions

if __name__ == '__main__':
    unittest.main() 