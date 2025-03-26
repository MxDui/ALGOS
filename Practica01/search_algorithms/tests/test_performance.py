import unittest
import random
from search_algorithms.algorithms import SearchAlgorithmFactory
from search_algorithms.utils import measure_time, run_performance_test

class TestPerformance(unittest.TestCase):
    
    def setUp(self):
        # Obtenemos todos los algoritmos de búsqueda
        self.algorithms = SearchAlgorithmFactory.get_all_algorithms()
        
        # Creamos arreglos de diferentes tamaños
        self.small_array = list(range(100))
        self.medium_array = list(range(1000))
        self.large_array = list(range(10000))
        
        # Creamos una copia desordenada del arreglo pequeño para testear busqueda lineal
        self.small_unsorted = self.small_array.copy()
        random.shuffle(self.small_unsorted)
        
    """Prueba para la función measure_time"""
    def test_measure_time(self):
        # Elegimos el algoritmo de búsqueda binaria
        binary_search = self.algorithms["binary"]
        
        # Medimos el tiempo de búsqueda de un elemento en el arreglo pequeño
        time_taken = measure_time(binary_search, self.small_array, 50, repetitions=10)
        
        # El tiempo tomado debe ser mayor a 0
        self.assertGreater(time_taken, 0)
        
        # Ponemos un valor muy pequeño aproximado a lo que debería tardar
        self.assertLess(time_taken, 0.001)
        
        """Compara la eficiencia de los algoritmos de búsqueda"""
    def test_algorithm_efficiency_comparison(self):
        # Elegimos un elemento cercano al final del arreglo mediano
        target = self.medium_array[900] 
        
        # Medimos el tiempo de búsqueda para cada algoritmo
        times = {}
        for name, algorithm in self.algorithms.items():
            times[name] = measure_time(algorithm, self.medium_array, target, repetitions=10)
            
        # La búsqueda Binaria, por interpolación, y exponencial deberían ser más rápidas que la lineal para arreglos ordenados
        self.assertLess(times["binary"], times["linear"])
        self.assertLess(times["exponential"], times["linear"])
        
        # La búsqueda binaria debería ser aproximadamente dos veces más rápida que la lineal
        self.assertLessEqual(times["binary"] * 2, times["linear"])
        
        """Prueba para la función run_performance_test"""
    def test_run_performance_test(self):
        sizes = [10, 100]
        results = run_performance_test(
            self.algorithms,
            sizes=sizes,
            repetitions=5,
            position='end'  # Buscamos los elememtos al final del arreglo, ya que es el peor caso en varios algoritmos
        )
        
        # Verificamos que el resultado tenga los nombres de los algoritmos
        for algo_name in self.algorithms.keys():
            self.assertIn(algo_name, results)
        
        # Verificamps que los tamaños se registraron correctamente
        self.assertIn('sizes', results)
        self.assertEqual(results['sizes'], sizes)
        
        # Verificamos que cada algoritmo tenga resultados para cada tamaño del arreglo
        for algo_name in self.algorithms.keys():
            # Verificamos la estructura de los resultados
            self.assertIn('times', results[algo_name])
            self.assertIn('iterations', results[algo_name])
            
            # Verificamos si las listas de 'times' e 'iteractions' tienen la longitud correcta
            self.assertEqual(len(results[algo_name]['times']), len(sizes))
            self.assertEqual(len(results[algo_name]['iterations']), len(sizes))
            
        # La búsqueda binaria debería tener menos iteraciones que la búsqueda lineal de arreglos grandes
        self.assertLess(
            results['binary']['iterations'][1],  # Iterations de la busqueda binaria para arreglos de tamaño 100
            results['linear']['iterations'][1]   # Iterations de la busqueda lineal para arreglos de tamaño 100
        )
        
        """Test para la búsqueda lineal en un arreglo desordenado"""
    def test_linear_search_with_unsorted_array(self):
        linear = self.algorithms["linear"]
        
        # Elegimos un valor que sabemos que está en el arreglo
        value = self.small_unsorted[20]
        
        # La busqueda debería encontrar el valor y devolver su índice
        index = linear.search(self.small_unsorted, value)
        self.assertNotEqual(index, -1)
        self.assertEqual(self.small_unsorted[index], value)

if __name__ == '__main__':
    unittest.main() 