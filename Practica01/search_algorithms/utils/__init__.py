"""
Paquete de Utilidades

Este paquete proporciona funciones de utilidad para los algoritmos de búsqueda.

Módulos:
    logger: Utilidades de registro
    performance: Utilidades de medición de rendimiento
"""

from .logger import get_console_logger, get_file_logger, get_null_logger
from .performance import measure_time, run_performance_test

__all__ = [
    'get_console_logger',
    'get_file_logger',
    'get_null_logger',
    'measure_time',
    'run_performance_test'
]
