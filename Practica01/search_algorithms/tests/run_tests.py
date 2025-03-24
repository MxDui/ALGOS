#!/usr/bin/env python3
"""
Ejecuta las Pruebas

Este script ejecuta todas las pruebas en el paquete search_algorithms.
"""

import unittest
import sys
import os

# Añade el directorio padre al sys.path para que las importaciones funcionen correctamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

"""Ejecuta todas las pruebas"""
def run_tests():
    loader = unittest.TestLoader()
    
    # Carga las pruebas desde el directorio de pruebas
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern="test_*.py")
    
    # Creamos un "ejecutor" de pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    
    # Ejecutamos las pruebas
    result = runner.run(suite)
    
    # Devolvemos el código de salida distinto de cero si las pruebas fallaron
    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code) 