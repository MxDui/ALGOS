#!/usr/bin/env python3
"""
Prueba de Rendimiento de Algoritmos de Búsqueda

Este script ejecuta pruebas de rendimiento en todos los algoritmos de búsqueda y genera
comparaciones visuales de los resultados.
"""

import os
import sys
import time
import logging
from typing import Dict, List, Any

from search_algorithms.algorithms import SearchAlgorithmFactory
from search_algorithms.utils import get_console_logger, get_file_logger, run_performance_test
from search_algorithms.visualization import save_plots

def setup_loggers():
    """Configuramos los loggers para la prueba de rendimiento"""
    # Creamos el directorio de los logs si no existe
    os.makedirs('logs', exist_ok=True)
    
    # Creamos un logger de consola
    console_logger = get_console_logger('performance_test')
    
    # Y creamos el logger de archivo
    file_logger = get_file_logger('performance_test', 'logs/performance_test.log')
    
    return console_logger, file_logger

"""Ejecuta pruebas de rendimiento en todos los algoritmos de búsqueda"""
def run_tests(console_logger, file_logger):
    console_logger.info("=== Comparación de Rendimiento de los Algoritmos de Búsqueda ===")
    file_logger.info("=== Iniciando la comparación de rendimiento ===")
    
    try:
        # Primero obtenemos todos los algoritmos (sin logging para evitar "contaminar" las mediciones de rendimiento)
        algorithms = SearchAlgorithmFactory.get_all_algorithms()
        
        # Definimos los tamaños de los arreglo a probar
        sizes = [100, 1000, 10000, 100000]
        if '--extended' in sys.argv:
            sizes.append(1000000)
        
        console_logger.info(f"Probando con tamaños de arreglo: {sizes}")
        file_logger.info(f"Probando con tamaños de arreglo: {sizes}")
        
        # Definimos los escenarios de prueba, los posibles casos, que son:
        scenarios = {
            'random': 'elemento en posición aleatoria',
            'start': 'elemento al inicio del arreglo',
            'middle': 'elemento en medio del arreglo',
            'end': 'elemento al final del arreglo'
        }
        
        # Ejecuta las pruebas para cada escenario
        for position, description in scenarios.items():
            console_logger.info(f"\nEjecutando pruebas con {description}...")
            file_logger.info(f"Ejecutando pruebas con {description}")
            
            # Ejecuta la prueba de rendimiento
            start_time = time.time()
            results = run_performance_test(algorithms, sizes, repetitions=100, position=position)
            end_time = time.time()
            
            # Registra los resultados más "generales"
            console_logger.info(f"Tiempo total de prueba: {end_time - start_time:.2f} segundos")
            file_logger.info(f"Tiempo total de prueba: {end_time - start_time:.2f} segundos")
            
            # Y registramos los resultados ya más detallados
            for size_idx, size in enumerate(sizes):
                console_logger.info(f"\nResultados para tamaño de arreglo {size}:")
                file_logger.info(f"Resultados para tamaño de arreglo {size}:")
                
                for algo_name in algorithms.keys():
                    time_result = results[algo_name]['times'][size_idx]
                    iter_result = results[algo_name]['iterations'][size_idx]
                    
                    console_logger.info(f"{algo_name.capitalize()}: {time_result:.6f} segundos, {iter_result} iteraciones")
                    file_logger.info(f"{algo_name.capitalize()}: {time_result:.6f} segundos, {iter_result} iteraciones")
            
            # Guardamos las gráficas que obtuvimos
            plot_dir = f"plots/{position}"
            plots = save_plots(
                results, 
                output_dir=plot_dir,
                time_plot_filename=f'time_comparison_{position}.png',
                iterations_plot_filename=f'iterations_comparison_{position}.png'
            )
            
            console_logger.info(f"\nGráficas guardadas en: {plot_dir}")
            file_logger.info(f"Gráficas guardadas en: {plot_dir}")
        
        console_logger.info("\n=== Comparación de rendimiento finalizada ===")
        file_logger.info("=== Comparación de rendimiento finalizada ===")
        
    except ImportError as e:
        console_logger.error(f"Error: {e}")
        file_logger.error(f"Error: {e}")
        console_logger.error("Asegúrese de tener instalada la biblioteca matplotlib: pip install matplotlib")
        file_logger.error("No se pudo importar matplotlib")

"""Función principal"""
def main():
    # coonfiguramos los loggers
    console_logger, file_logger = setup_loggers()
    
    try:
        # Ejecutamos las pruebas
        run_tests(console_logger, file_logger)
    except KeyboardInterrupt:
        console_logger.info("\nPruebas interrumpidas por el usuario.")
        file_logger.info("Pruebas interrumpidas por el usuario.")
        sys.exit(0)
    except Exception as e:
        console_logger.error(f"Error inesperado: {e}")
        file_logger.error(f"Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 