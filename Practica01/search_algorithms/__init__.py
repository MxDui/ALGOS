"""
Paquete de Algoritmos de Búsqueda

Este paquete proporciona implementaciones de varios algoritmos de búsqueda
y utilidades para medir y visualizar su rendimiento.

Paquetes:
    algorithms: Implementaciones de algoritmos de búsqueda
    utils: Funciones de utilidad
    visualization: Utilidades de visualización

Ejemplo de uso:
    from search_algorithms.algorithms import SearchAlgorithmFactory
    from search_algorithms.utils import get_console_logger
    
    # Crear un logger
    logger = get_console_logger("search_demo")
    
    # Obtener un algoritmo de búsqueda
    binary_search = SearchAlgorithmFactory.get_algorithm("binary", logger)
    
    # Usar el algoritmo
    result = binary_search.search([1, 2, 3, 4, 5], 3)
    print(f"Encontrado en el índice: {result}")
"""

__version__ = '1.0.0'

from .algorithms import (
    SearchAlgorithm,
    LinearSearch,
    BinarySearch,
    ExponentialSearch,
    InterpolationSearch,
    SearchAlgorithmFactory
)

from .utils import (
    get_console_logger,
    get_file_logger,
    get_null_logger,
    measure_time,
    run_performance_test
)

from .visualization import (
    plot_time_comparison,
    plot_iterations_comparison,
    save_plots
)

__all__ = [
    'SearchAlgorithm',
    'LinearSearch',
    'BinarySearch',
    'ExponentialSearch',
    'InterpolationSearch',
    'SearchAlgorithmFactory',
    'get_console_logger',
    'get_file_logger',
    'get_null_logger',
    'measure_time',
    'run_performance_test',
    'plot_time_comparison',
    'plot_iterations_comparison',
    'save_plots'
]