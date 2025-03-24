"""
Utilidades de Registro (Logging)

Este módulo proporciona configuración de registro para el paquete de algoritmos de búsqueda.

Funciones:
    get_console_logger: Configura y devuelve un logger para la salida por consola
    get_file_logger: Configura y devuelve un logger para la salida a un archivo
    get_null_logger: Devuelve un logger que no produce ninguna salida
"""

import logging
import os
from typing import Optional

"""
    Configura y devuelve un logger para la salida por consola.
    
    Args:
        name (str): Nombre del logger
        level (int): Nivel de registro (por defecto: logging.INFO)
        
    Returns:
        logging.Logger: Instancia de logger configurada
    """
def get_console_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    # Creamos un logger
    logger = logging.getLogger(f"{name}_console")
    logger.setLevel(level)
    
    # Evitamos la duplicación de handlers
    if not logger.handlers:
        # Creamos el handler de consola
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        
        # Establecemso el formato
        formatter = logging.Formatter('%(message)s')
        console_handler.setFormatter(formatter)
        
        # Añadimos el handler al logger
        logger.addHandler(console_handler)
    
    return logger

"""
    Configura y devuelve un logger para la salida a unn archivo.
    
    Args:
        name (str): Nombre del logger
        filename (str): Ruta al archivo de log
        level (int): Nivel de registro (por defecto: logging.INFO)
        
    Returns:
        logging.Logger: Instancia de logger configurada
    """
def get_file_logger(name: str, filename: str, level: int = logging.INFO) -> logging.Logger:
    # Creamos el logger
    logger = logging.getLogger(f"{name}_file")
    logger.setLevel(level)
    
    # Creamos el directorio de logs si no existe
    os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
    
    # Evitamos la duplicación de handlers
    if not logger.handlers:
        # Creamos el handler de archivo
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(level)
        
        # Establecemos el formato
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        # Añadimos el handler al logger
        logger.addHandler(file_handler)
    
    return logger

"""
    Devuelve un logger que no produce ninguna salida.
    
    Args:
        name (str): Nombre del logger
        
    Returns:
        logging.Logger: Instancia de logger sin handlers
    """
def get_null_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(f"{name}_null")
    logger.setLevel(logging.CRITICAL + 1)  # Por encima de todos los niveles estándar de logging
    return logger 