"""
Módulo de configuración del logger

Este módulo proporciona una configuración centralizada para el logger
que será utilizado por todos los scripts de búsqueda.
"""

import logging

def setup_logger(name):
    """
    Configura y devuelve un logger con el nombre especificado.
    
    Args:
        name (str): Nombre del logger
        
    Returns:
        logging.Logger: Logger configurado
    """
    # Crear logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Evitar duplicación de handlers si el logger ya existe
    if not logger.handlers:
        # Crear un manejador para la consola
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Definir el formato de los mensajes
        formatter = logging.Formatter('%(message)s')
        console_handler.setFormatter(formatter)
        
        # Agregar el manejador al logger
        logger.addHandler(console_handler)
    
    return logger

def get_file_logger(name, filename):
    """
    Configura y devuelve un logger que escribe en un archivo.
    
    Args:
        name (str): Nombre del logger
        filename (str): Nombre del archivo de log
        
    Returns:
        logging.Logger: Logger configurado
    """
    # Crear logger
    logger = logging.getLogger(f"{name}_file")
    logger.setLevel(logging.INFO)
    
    # Evitar duplicación de handlers si el logger ya existe
    if not logger.handlers:
        # Crear un manejador para el archivo
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(logging.INFO)
        
        # Definir el formato de los mensajes
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        # Agregar el manejador al logger
        logger.addHandler(file_handler)
    
    return logger 