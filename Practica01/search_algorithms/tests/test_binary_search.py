import unittest
from search_algorithms.algorithms import BinarySearch

class TestBinarySearch(unittest.TestCase):
    
    def setUp(self):
        self.search = BinarySearch()
    
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
        
    """Test para cuando hay duplicados"""
    def test_array_with_duplicates(self):
        arr = [1, 2, 2, 2, 3, 4, 5]
        result = self.search.search(arr, 2)
        self.assertIn(result, [1, 2, 3])  # Could be any of these positions
        
    """Test para el contador de iteraciones de búsqueda binaria"""
    def test_iteration_count(self):
        arr = [i for i in range(16)]
        
        # Elemento del medio
        self.search.search(arr, 8)
        self.assertLessEqual(self.search.iterations, 4)  # log2(16) = 4
        
        # Peor caso (que no está en el arreglo)
        self.search.search(arr, 20)
        self.assertLessEqual(self.search.iterations, 5)  # log2(16) + 1 = 5
        
    """Test para la función search_range"""
    def test_search_range(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        # Busca en un "subrango" del arreglo
        result = self.search.search_range(arr, 4, 2, 6, 0)
        self.assertEqual(result, 3)
        
        # Elemento fuera del rango especificado
        result = self.search.search_range(arr, 9, 0, 5, 0)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main() 