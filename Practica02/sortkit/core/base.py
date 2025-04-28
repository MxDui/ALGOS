from typing import Protocol, TypeVar, List, Generator, Callable, Any, Union, cast, overload
import functools
import copy

T = TypeVar('T')


class SortAlgorithm(Protocol):
    """Protocolo que define la interfaz para todos los algoritmos de ordenación."""
    
    def __call__(
        self, data: List[int], trace: bool = False
    ) -> Union[List[int], Generator[List[int], None, List[int]]]:
        """
        Ordena la lista de entrada.
        
        Args:
            data: La lista a ordenar
            trace: Si es True, genera estados intermedios durante la ordenación
                  Si es False, solo devuelve la lista ordenada final
                  
        Returns:
            Si trace es False, devuelve la lista ordenada
            Si trace es True, genera un generador de estados intermedios,
            siendo el estado final la lista ordenada
        """
        ...


def traceable(func: Callable) -> Callable:
    """
    Decorador que añade capacidad de seguimiento a funciones de ordenación.
    
    Cuando trace=True, la función decorada generará estados intermedios
    a medida que avanza el algoritmo de ordenación.
    
    Cuando trace=False, la función decorada simplemente devolverá la
    lista ordenada final.
    
    Args:
        func: La función de ordenación a decorar
        
    Returns:
        Una función envuelta que puede devolver una lista ordenada o
        generar estados intermedios
    """
    @functools.wraps(func)
    def wrapper(data: List[int], trace: bool = False) -> Union[List[int], Generator[List[int], None, List[int]]]:
        # Hacer una copia de los datos de entrada para evitar modificar el original
        data_copy = copy.deepcopy(data)
        
        if not trace:
            # Si el seguimiento está desactivado, simplemente llamar a la función original
            return func(data_copy)
        
        # Si el seguimiento está habilitado, envolver la función para generar estados intermedios
        def trace_generator() -> Generator[List[int], None, List[int]]:
            # Generar el estado inicial
            yield copy.deepcopy(data_copy)
            
            # Llamar a la función de ordenación
            result = func(data_copy)
            
            # Generar el resultado final ordenado
            yield copy.deepcopy(result)
            
            return result
        
        return trace_generator()
    
    # Añadir un indicador para mostrar que esta función ha sido decorada
    wrapper.is_traceable = True
    
    return wrapper
