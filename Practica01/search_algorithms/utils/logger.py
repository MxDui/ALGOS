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
from colorama import init, Fore, Style

# Initialize colorama
init()

class ColoredFormatter(logging.Formatter):
    """Formateador personalizado que añade colores y emojis a los mensajes de registro."""
    
    # Diccionario de emojis para cada algoritmo
    ALGORITHM_EMOJIS = {
        'Búsqueda Binaria': '🔍',
        'Búsqueda Lineal': '➡️',
        'Búsqueda Exponencial': '📈',
        'Búsqueda por Interpolación': '📊'
    }

    # Diccionario de emojis para diferentes tipos de mensajes
    MESSAGE_EMOJIS = {
        'Iteración': '🔄',
        'Comparando': '⚖️',
        'Realizando búsqueda binaria': '🎯',
        'Comprobando posición': '📍',
        'bajo': '⬇️',
        'alto': '⬆️',
        'pos': '📌',
        'izquierda': '⬅️',
        'derecha': '➡️',
        'medio': '↔️'
    }
    
    def format(self, record):
        # Get the original message
        message = record.getMessage()
        
        # Add colors and emojis based on the content
        if "Iteración" in message:
            # Format: "Iteración X: ..."
            parts = message.split(":")
            iteration = parts[0]
            rest = ":".join(parts[1:])
            colored_message = f"{Fore.CYAN}{self.MESSAGE_EMOJIS['Iteración']} {iteration}{Style.RESET_ALL}:{Fore.WHITE}{rest}{Style.RESET_ALL}"
        elif "Comparando" in message:
            # Format: "... Comparando X con Y"
            try:
                before, comparison = message.split("Comparando")
                values = comparison.strip()
                val1, val2 = values.split(" con ")
                colored_message = f"{Fore.CYAN}{before.strip()}{Style.RESET_ALL} {self.MESSAGE_EMOJIS['Comparando']} Comparando {Fore.YELLOW}{val1}{Style.RESET_ALL} con {Fore.YELLOW}{val2}{Style.RESET_ALL}"
            except:
                colored_message = f"{Fore.CYAN}{message}{Style.RESET_ALL}"
        elif "Realizando búsqueda binaria" in message:
            # Format: "Realizando búsqueda binaria en el rango [X, Y]"
            colored_message = f"\n{Fore.MAGENTA}{self.MESSAGE_EMOJIS['Realizando búsqueda binaria']} {message}{Style.RESET_ALL}"
        elif "Comprobando posición" in message:
            # Format: "Comprobando posición X, valor Y"
            try:
                before, values = message.split(", ")
                pos = before.split("posición")[1].strip()
                val = values.split("valor")[1].strip()
                colored_message = f"{self.MESSAGE_EMOJIS['Comprobando posición']} Comprobando posición {Fore.YELLOW}{pos}{Style.RESET_ALL}, valor {Fore.YELLOW}{val}{Style.RESET_ALL}"
            except:
                colored_message = f"{Fore.CYAN}{message}{Style.RESET_ALL}"
        elif any(key in message.lower() for key in ['bajo', 'alto', 'pos']):
            # Format: "bajo=X, pos=Y, alto=Z"
            try:
                parts = message.split(",")
                colored_parts = []
                for part in parts:
                    key, value = part.strip().split("=")
                    key = key.strip().lower()
                    emoji = self.MESSAGE_EMOJIS.get(key, '')
                    colored_parts.append(f"{emoji} {key}={Fore.YELLOW}{value}{Style.RESET_ALL}")
                colored_message = ", ".join(colored_parts)
            except:
                colored_message = f"{Fore.CYAN}{message}{Style.RESET_ALL}"
        elif any(key in message.lower() for key in ['izquierda', 'derecha', 'medio']):
            # Format: "izquierda=X, medio=Y, derecha=Z"
            try:
                parts = message.split(",")
                colored_parts = []
                for part in parts:
                    key, value = part.strip().split("=")
                    key = key.strip().lower()
                    emoji = self.MESSAGE_EMOJIS.get(key, '')
                    colored_parts.append(f"{emoji} {key}={Fore.YELLOW}{value}{Style.RESET_ALL}")
                colored_message = ", ".join(colored_parts)
            except:
                colored_message = f"{Fore.CYAN}{message}{Style.RESET_ALL}"
        elif any(algo in message for algo in self.ALGORITHM_EMOJIS.keys()):
            # Add emoji for algorithm names
            for algo, emoji in self.ALGORITHM_EMOJIS.items():
                if algo in message:
                    colored_message = f"\n{Fore.GREEN}{emoji} {message}{Style.RESET_ALL}"
                    break
            else:
                colored_message = f"{Fore.GREEN}{message}{Style.RESET_ALL}"
        else:
            colored_message = message
            
        return colored_message

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
        
        # Establecemos el formato con colores
        formatter = ColoredFormatter()
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