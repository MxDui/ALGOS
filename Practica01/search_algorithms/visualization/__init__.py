"""
Paquete de Visualización

Este paquete proporciona utilidades para visualizar el rendimiento de algoritmos.

Módulos:
    performance_plots: Utilidades para graficar métricas de rendimiento
"""

from .performance_plots import plot_time_comparison, plot_iterations_comparison, save_plots

__all__ = [
    'plot_time_comparison', 
    'plot_iterations_comparison', 
    'save_plots'
]
