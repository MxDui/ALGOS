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
    
    def test_get_algorithm(self):
        """Prueba para obtener algoritmos por nombre"""
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
        
    def test_get_all_algorithms(self):
        """Prueba para obtener todos los algoritmos"""
        algorithms = SearchAlgorithmFactory.get_all_algorithms()
        
        # Verificar que obtenemos el número correcto de algoritmos
        self.assertEqual(len(algorithms), 4)
        
        # Verificar que cada algoritmo es del tipo correcto
        self.assertIsInstance(algorithms["linear"], LinearSearch)
        self.assertIsInstance(algorithms["binary"], BinarySearch)
        self.assertIsInstance(algorithms["exponential"], ExponentialSearch)
        self.assertIsInstance(algorithms["interpolation"], InterpolationSearch)
        
    def test_register_algorithm(self):
        """Prueba para registrar un nuevo algoritmo"""
        # Registrar un algoritmo simulado
        SearchAlgorithmFactory.register_algorithm("mock", MockSearchAlgorithm)
        
        # Verificar que fue añadido
        mock_algo = SearchAlgorithmFactory.get_algorithm("mock")
        self.assertIsInstance(mock_algo, MockSearchAlgorithm)
        
        # Limpiar después de la prueba
        if "mock" in SearchAlgorithmFactory._algorithms:
            del SearchAlgorithmFactory._algorithms["mock"]
            
    def test_with_logger(self):
        """Prueba para crear algoritmos con un logger"""
        logger = logging.getLogger("test_logger")
        
        # Obtener algoritmo con logger
        binary = SearchAlgorithmFactory.get_algorithm("binary", logger)
        
        # Verificar que se estableció el logger
        self.assertEqual(binary.logger, logger)
        
    def test_get_available_algorithms(self):
        """Prueba para obtener nombres de algoritmos disponibles"""
        algorithms = SearchAlgorithmFactory.get_available_algorithms()
        
        # Verificar que la lista contiene los algoritmos esperados
        self.assertIn("linear", algorithms)
        self.assertIn("binary", algorithms)
        self.assertIn("exponential", algorithms)
        self.assertIn("interpolation", algorithms)
        
        # Verificar la longitud
        self.assertEqual(len(algorithms), 4)

if __name__ == '__main__':
    unittest.main() 