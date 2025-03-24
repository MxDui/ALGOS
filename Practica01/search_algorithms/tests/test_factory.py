import unittest
import logging
from search_algorithms.algorithms import (
    SearchAlgorithmFactory,
    LinearSearch,
    BinarySearch,
    ExponentialSearch,
    InterpolationSearch,
    SearchAlgorithm
)

class MockSearchAlgorithm(SearchAlgorithm):
    """Algoritmo de búsqueda simulado para probar el registro"""
    
    def __init__(self, logger=None):
        super().__init__("Mock Algorithm", logger)
    
    def search(self, arr, target):
        self._iterations += 1
        return 0

class TestSearchAlgorithmFactory(unittest.TestCase):
    
    """Prueba para obtener algoritmos por nombre"""
    def test_get_algorithm(self):
        # Prueba con nombres en minúsculas
        linear = SearchAlgorithmFactory.get_algorithm("linear")
        self.assertIsInstance(linear, LinearSearch)
        
        binary = SearchAlgorithmFactory.get_algorithm("binary")
        self.assertIsInstance(binary, BinarySearch)
        
        exponential = SearchAlgorithmFactory.get_algorithm("exponential")
        self.assertIsInstance(exponential, ExponentialSearch)
        
        interpolation = SearchAlgorithmFactory.get_algorithm("interpolation")
        self.assertIsInstance(interpolation, InterpolationSearch)
        
        # Prueba con mayúsculas y minúsculas mezcladas
        binary_mixed = SearchAlgorithmFactory.get_algorithm("BiNaRy")
        self.assertIsInstance(binary_mixed, BinarySearch)
        
        # Prueba con nombre inválido
        invalid = SearchAlgorithmFactory.get_algorithm("invalid_algorithm")
        self.assertIsNone(invalid)
        
    """Prueba para obtener todos los algoritmos"""
    def test_get_all_algorithms(self):
        algorithms = SearchAlgorithmFactory.get_all_algorithms()
        
        # Verificamos que obtenemos el número correcto de algoritmos
        self.assertEqual(len(algorithms), 4)
        
        # Verificamos que cada algoritmo es del tipo correcto
        self.assertIsInstance(algorithms["linear"], LinearSearch)
        self.assertIsInstance(algorithms["binary"], BinarySearch)
        self.assertIsInstance(algorithms["exponential"], ExponentialSearch)
        self.assertIsInstance(algorithms["interpolation"], InterpolationSearch)
        
    """Prueba para registrar un nuevo algoritmo"""
    def test_register_algorithm(self):
        # Registramos un algoritmo simulado
        SearchAlgorithmFactory.register_algorithm("mock", MockSearchAlgorithm)
        
        # Verificamos que fue añadido
        mock_algo = SearchAlgorithmFactory.get_algorithm("mock")
        self.assertIsInstance(mock_algo, MockSearchAlgorithm)
        
        # Limpiamos después de la prueba
        if "mock" in SearchAlgorithmFactory._algorithms:
            del SearchAlgorithmFactory._algorithms["mock"]
            
    """Prueba para crear algoritmos con un logger"""
    def test_with_logger(self):
        logger = logging.getLogger("test_logger")
        
        # Obtenemos el algoritmo con logger
        binary = SearchAlgorithmFactory.get_algorithm("binary", logger)
        
        # Verificamos que se estableció el logger
        self.assertEqual(binary.logger, logger)
        
    """Prueba para obtener los nombres de los algoritmos disponibles"""
    def test_get_available_algorithms(self):
        algorithms = SearchAlgorithmFactory.get_available_algorithms()
        
        # Verificamos que la lista contenga los algoritmos esperados
        self.assertIn("linear", algorithms)
        self.assertIn("binary", algorithms)
        self.assertIn("exponential", algorithms)
        self.assertIn("interpolation", algorithms)
        
        # Verificamos la longitud
        self.assertEqual(len(algorithms), 4)

if __name__ == '__main__':
    unittest.main() 