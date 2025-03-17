#!/usr/bin/env python3
"""
Ejecutor de Pruebas

Este script descubre y ejecuta todas las pruebas en el paquete search_algorithms.
"""

import unittest
import sys
import os

# Añadir el directorio padre al sys.path para que las importaciones funcionen correctamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def run_tests():
    """Descubrir y ejecutar todas las pruebas"""
    loader = unittest.TestLoader()
    
    # Cargar pruebas desde el directorio de pruebas
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern="test_*.py")
    
    # Crear un ejecutor de pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    
    # Ejecutar pruebas
    result = runner.run(suite)
    
    # Devolver código de salida distinto de cero si las pruebas fallaron
    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code) 