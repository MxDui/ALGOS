import unittest
from search_algorithms.algorithms import ExponentialSearch

class TestExponentialSearch(unittest.TestCase):
    
    def setUp(self):
        self.search = ExponentialSearch()
    
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
        
    """Test con un arreglo más grande para verificar el comportamiento exponencial"""
    def test_large_array(self):
        arr = [i for i in range(100)]
        
        # Elemento en la primera mitad
        result = self.search.search(arr, 30)
        self.assertEqual(result, 30)
        
        # Elemento en la segunda mitad
        result = self.search.search(arr, 80)
        self.assertEqual(result, 80)
        
    """Test para cuando hay duplicados"""
    def test_array_with_duplicates(self):
        arr = [1, 2, 2, 2, 3, 4, 5]
        result = self.search.search(arr, 2)
        self.assertIn(result, [1, 2, 3]) 
        
    """Test de eficiencia de la busqueda exponencial"""
    def test_iteration_efficiency(self):
        # Creamos un arreglo más grande ordenado
        arr = [i for i in range(1024)]  # 2^10
        
        # Elemento al final
        self.search.search(arr, 1000)
        
        # Para una búsqueda exponencial, el número de iteraciones debería ser
        # significativamente menos de lo que requeriría la búsqueda lineal (1000)
        self.assertLess(self.search.iterations, 50)

if __name__ == '__main__':
    unittest.main() 