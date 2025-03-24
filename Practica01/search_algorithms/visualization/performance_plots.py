"""
Utilidades de Visualización de Rendimiento

Este módulo proporciona utilidades para visualizar el rendimiento de los algoritmos de búsqueda.

Funciones:
    plot_time_comparison: Grafica la comparación de tiempo de los algoritmos de búsqueda
    plot_iterations_comparison: Grafica la comparación de iteraciones de los algoritmos de búsqueda
    save_plots: Guarda las gráficas en archivos
"""

import os
from typing import Dict, List, Any, Optional
import matplotlib.pyplot as plt


"""
    Grafica la comparación de tiempo de los algoritmos de búsqueda.
    
    Args:
        results (Dict[str, Dict[str, Any]]): Resultados de pruebas de rendimiento
        title (str, optional): Título de la gráfica. Por defecto 'Comparación de Tiempo de Algoritmos de Búsqueda'.
        log_scale (bool, optional): Si se debe usar escala logarítmica. Por defecto True.
        figure_size (tuple, optional): Tamaño de la figura (ancho, alto). Por defecto (12, 6).
        
    Returns:
        plt.Figure: La figura generada
    """
def plot_time_comparison(
    results: Dict[str, Dict[str, Any]], 
    title: str = 'Comparación de Tiempo de Algoritmos de Búsqueda',
    log_scale: bool = True,
    figure_size: tuple = (12, 6)
) -> plt.Figure:

    sizes = results.get('sizes', [])
    
    if not sizes:
        raise ValueError("No se encontró información de tamaño en los resultados")
    
    # Creamos la figura y sus ejes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figure_size)
    
    # Grafica la comparación de tiempo (escala lineal)
    for name, data in results.items():
        if name != 'sizes' and 'times' in data:
            ax1.plot(sizes, data['times'], marker='o', label=name)
    
    ax1.set_title(f'{title} (Escala Lineal)')
    ax1.set_xlabel('Tamaño del Array')
    ax1.set_ylabel('Tiempo (segundos)')
    ax1.grid(True)
    ax1.legend()
    
    # Grafica la comparación de tiempo (escala logarítmica si se solicita)
    for name, data in results.items():
        if name != 'sizes' and 'times' in data:
            ax2.plot(sizes, data['times'], marker='o', label=name)
    
    ax2.set_title(f'{title} (Escala Logarítmica)')
    ax2.set_xlabel('Tamaño del Array')
    ax2.set_ylabel('Tiempo (segundos)')
    ax2.grid(True)
    if log_scale:
        ax2.set_xscale('log')
        ax2.set_yscale('log')
    
    plt.tight_layout()
    return fig

"""
    Grafica la comparación de iteraciones de los algoritmos de búsqueda.
    
    Args:
        results (Dict[str, Dict[str, Any]]): Resultados de pruebas de rendimiento
        title (str, optional): Título de la gráfica. Por defecto 'Comparación de Iteraciones de Algoritmos de Búsqueda'.
        log_scale (bool, optional): Si se debe usar escala logarítmica. Por defecto True.
        figure_size (tuple, optional): Tamaño de la figura (ancho, alto). Por defecto (12, 6).
        
    Returns:
        plt.Figure: La figura generada
    """
def plot_iterations_comparison(
    results: Dict[str, Dict[str, Any]], 
    title: str = 'Comparación de Iteraciones de Algoritmos de Búsqueda',
    log_scale: bool = True,
    figure_size: tuple = (12, 6)
) -> plt.Figure:
    sizes = results.get('sizes', [])
    
    if not sizes:
        raise ValueError("No se encontró información de tamaño en los resultados")
    
    # Creamos la figura y sus ejes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figure_size)
    
    # Graficamos la comparación de iteraciones (escala lineal)
    for name, data in results.items():
        if name != 'sizes' and 'iterations' in data:
            ax1.plot(sizes, data['iterations'], marker='o', label=name)
    
    ax1.set_title(f'{title} (Escala Lineal)')
    ax1.set_xlabel('Tamaño del Array')
    ax1.set_ylabel('Número de Iteraciones')
    ax1.grid(True)
    ax1.legend()
    
    # Graficamos la comparación de iteraciones (escala logarítmica si se solicita)
    for name, data in results.items():
        if name != 'sizes' and 'iterations' in data:
            ax2.plot(sizes, data['iterations'], marker='o', label=name)
    
    ax2.set_title(f'{title} (Escala Logarítmica)')
    ax2.set_xlabel('Tamaño del Array')
    ax2.set_ylabel('Número de Iteraciones')
    ax2.grid(True)
    if log_scale:
        ax2.set_xscale('log')
        ax2.set_yscale('log')
    
    plt.tight_layout()
    return fig

"""
    Guarda las gráficas de rendimiento en archivos.
    
    Args:
        results (Dict[str, Dict[str, Any]]): Resultados de pruebas de rendimiento
        output_dir (str, optional): Directorio de salida. Por defecto 'plots'.
        time_plot_filename (str, optional): Nombre del archivo de la gráfica de tiempo. Por defecto 'time_comparison.png'.
        iterations_plot_filename (str, optional): Nombre del archivo de la gráfica de iteraciones. Por defecto 'iterations_comparison.png'.
        dpi (int, optional): DPI para las imágenes de salida. Por defecto 300.
        
    Returns:
        List[str]: Lista de rutas a archivos guardados de las gráficas
    """
def save_plots(
    results: Dict[str, Dict[str, Any]], 
    output_dir: str = 'plots',
    time_plot_filename: str = 'time_comparison.png',
    iterations_plot_filename: str = 'iterations_comparison.png',
    dpi: int = 300
) -> List[str]:
    # Creamos el directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    saved_files = []
    
    # Guardamos la gráfica de comparación de tiempo
    time_fig = plot_time_comparison(results)
    time_path = os.path.join(output_dir, time_plot_filename)
    time_fig.savefig(time_path, dpi=dpi)
    plt.close(time_fig)
    saved_files.append(time_path)
    
    # Guardamos la gráfica de comparación de iteraciones
    iter_fig = plot_iterations_comparison(results)
    iter_path = os.path.join(output_dir, iterations_plot_filename)
    iter_fig.savefig(iter_path, dpi=dpi)
    plt.close(iter_fig)
    saved_files.append(iter_path)
    
    return saved_files 