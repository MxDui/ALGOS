import sys
import random
import time
from typing import List, Optional, Any, Dict
from sortkit.registry import ALGORITHMS, list_algorithms, get_algorithm
from sortkit.structs.dllist import DoublyLinkedList

def generate_random_data(size: int, seed: Optional[int] = None) -> List[int]:
    """
    Genera una lista de enteros aleatorios.
    
    Args:
        size: Número de elementos a generar
        seed: Semilla aleatoria para reproducibilidad
        
    Returns:
        Una lista de enteros aleatorios
    """
    if seed is not None:
        random.seed(seed)
    return [random.randint(0, 100) for _ in range(size)]


def print_steps(steps: List[List[int]]) -> None:
    """
    Imprime los pasos de ordenación en un formato legible.
    
    Args:
        steps: Lista de listas, cada una representando un paso en el proceso de ordenación
    """
    # No mostrar todos los pasos para listas grandes para evitar salida abrumadora
    total_steps = len(steps)
    
    # Mostrar un número razonable de pasos
    if total_steps <= 2:
        print("Solo se capturaron estados inicial y final:")
        print(f"Inicial: {steps[0]}")
        print(f"Final:   {steps[-1]}")
    else:
        print(f"Total de pasos: {total_steps}")
        print(f"Inicial: {steps[0]}")
        
        # Para listas pequeñas, mostrar todos los pasos
        if total_steps <= 10:
            for i in range(1, total_steps - 1):
                print(f"Paso {i}: {steps[i]}")
        else:
            # Para recuentos de pasos más grandes, mostrar ~8 pasos distribuidos uniformemente
            num_to_show = min(8, total_steps - 2)
            step_interval = (total_steps - 2) // num_to_show
            
            for i in range(1, total_steps - 1, step_interval):
                print(f"Paso {i}: {steps[i]}")
                
            # Asegurarse de mostrar el último paso intermedio si aún no lo hemos hecho
            if 1 + step_interval * (num_to_show - 1) < total_steps - 1:
                print(f"Paso {total_steps - 2}: {steps[total_steps - 2]}")
        
        print(f"Final:   {steps[-1]}")


def run_algorithm(algorithm_name: str, size: int, trace: bool, seed: Optional[int], use_linked_list: bool = False) -> None:
    """
    Ejecuta un algoritmo de ordenación y muestra los resultados.
    
    Args:
        algorithm_name: Nombre del algoritmo a ejecutar
        size: Tamaño del array de entrada
        trace: Si se debe mostrar el seguimiento paso a paso
        seed: Semilla aleatoria para reproducibilidad
        use_linked_list: Si se debe usar la implementación de lista enlazada
    """
    algorithm = get_algorithm(algorithm_name, use_linked_list=use_linked_list)
    data = generate_random_data(size, seed)
    
    # Convertir a lista enlazada si es necesario
    if use_linked_list:
        input_data = DoublyLinkedList(data)
        print(f"\nEjecutando ordenación {algorithm_name.capitalize()} en lista enlazada de tamaño {size}")
    else:
        input_data = data
        print(f"\nEjecutando ordenación {algorithm_name.capitalize()} en lista de tamaño {size}")
    
    print(f"Entrada: {data}")
    
    if trace:
        start_time = time.perf_counter()
        steps = list(algorithm(input_data, trace=True))
        end_time = time.perf_counter()
        
        print(f"\nPasos de ordenación:")
        # Convertir pasos de lista enlazada a listas regulares para visualización
        if use_linked_list:
            list_steps = [step.to_list() for step in steps]
            print_steps(list_steps)
        else:
            print_steps(steps)
    else:
        start_time = time.perf_counter()
        result = algorithm(input_data)
        end_time = time.perf_counter()
        
        # Convertir resultado a lista regular para visualización
        if use_linked_list:
            result_list = result.to_list()
            print(f"Salida: {result_list}")
        else:
            print(f"Salida: {result}")
    
    elapsed = end_time - start_time
    print(f"\nTiempo transcurrido: {elapsed:.6f} segundos")


def run_demo(size: int, trace: bool, seed: Optional[int], use_linked_list: bool = False) -> None:
    """
    Ejecuta una demostración de todos los algoritmos de ordenación.
    
    Args:
        size: Tamaño del array de entrada
        trace: Si se debe mostrar el seguimiento paso a paso
        seed: Semilla aleatoria para reproducibilidad
        use_linked_list: Si se debe usar la implementación de lista enlazada
    """
    implementation = "Lista Enlazada" if use_linked_list else "Array"
    print(f"\n===== DEMOSTRACIÓN DE SORTKIT (Implementación de {implementation}) =====\n")
    
    # Asegurar que se usen los mismos datos para todos los algoritmos en la demostración
    if seed is not None:
        random.seed(seed)
    data = generate_random_data(size)
    
    # Convertir a lista enlazada si es necesario
    if use_linked_list:
        input_data = DoublyLinkedList(data)
    else:
        input_data = data.copy()
    
    for algorithm_name in list_algorithms():
        algorithm = get_algorithm(algorithm_name, use_linked_list=use_linked_list)
        
        print(f"\n--- Ordenación {algorithm_name.capitalize()} ---")
        print(f"Entrada: {data}")
        
        if trace:
            start_time = time.perf_counter()
            if use_linked_list:
                # Crear una nueva lista enlazada para cada algoritmo
                algo_input = DoublyLinkedList(data)
                steps = list(algorithm(algo_input, trace=True))
                # Convertir pasos de lista enlazada a listas regulares para visualización
                list_steps = [step.to_list() for step in steps]
            else:
                steps = list(algorithm(data.copy(), trace=True))
                list_steps = steps
            end_time = time.perf_counter()
            
            print("\nPasos de ordenación:")
            print_steps(list_steps)
        else:
            start_time = time.perf_counter()
            if use_linked_list:
                # Crear una nueva lista enlazada para cada algoritmo
                algo_input = DoublyLinkedList(data)
                result = algorithm(algo_input)
                result_list = result.to_list()
            else:
                result = algorithm(data.copy())
                result_list = result
            end_time = time.perf_counter()
            
            print(f"Salida: {result_list}")
        
        elapsed = end_time - start_time
        print(f"Tiempo transcurrido: {elapsed:.6f} segundos\n")
        print("-" * 50)


if __name__ == "__main__":
    # Usar un tamaño pequeño para mostrar mejor los pasos del algoritmo
    size = 8
    trace = True
    seed = 42
    
    # Ejecutar con implementación de array
    run_demo(size=size, trace=trace, seed=seed, use_linked_list=False)
    
    # Ejecutar con implementación de lista enlazada
    run_demo(size=size, trace=trace, seed=seed, use_linked_list=True)