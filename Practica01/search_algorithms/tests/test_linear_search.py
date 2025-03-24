import unittest
from search_algorithms.algorithms import LinearSearch

class TestLinearSearch(unittest.TestCase):
    
    def setUp(self):
        self.search = LinearSearch()
    
    """Pruebas para las busquedas en arreglos vacios"""
    def test_empty_array(self):
        result = self.search.search([], 5)
        self.assertEqual(result, -1)
        
    """Test para cuando encontremos un elemento en el principio del arreglo"""
    def test_element_at_beginning(self):
        arr = [5, 2, 4, 6, 8]
        result = self.search.search(arr, 5)
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
        
    """Test para cuando hay elementos duplicados"""
    def test_duplicate_elements(self):
        arr = [1, 2, 2, 3, 4, 2]
        result = self.search.search(arr, 2)
        self.assertEqual(result, 1)
        
    """Test para contar las iteraciones de la busqueda lineal""" 
    def test_iteration_count(self):
        arr = [1, 2, 3, 4, 5]
        
        # elemento al inicio
        self.search.search(arr, 1)
        self.assertEqual(self.search.iterations, 1)
        
        # Elemento a la mitad
        self.search.search(arr, 3)
        self.assertEqual(self.search.iterations, 3)
        
        # Elemento que no está en el arreglo
        self.search.search(arr, 6)
        self.assertEqual(self.search.iterations, 5)

if __name__ == '__main__':
    unittest.main() 