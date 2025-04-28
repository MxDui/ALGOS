from typing import List, Optional, Iterator, TypeVar, Generic, Any, Union, Callable, Dict, Generator
import copy
import functools

T = TypeVar('T')


class Node(Generic[T]):
    """Un nodo en una lista doblemente enlazada."""
    
    def __init__(self, value: T) -> None:
        """
        Inicializa un nuevo nodo.
        
        Args:
            value: El valor a almacenar en el nodo
        """
        self.value = value
        self.prev: Optional[Node[T]] = None
        self.next: Optional[Node[T]] = None


class DoublyLinkedList(Generic[T]):
    """
    Una implementación de lista doblemente enlazada.
    
    Esta clase proporciona una interfaz similar a una lista para una estructura de datos de lista doblemente enlazada,
    con métodos que imitan las operaciones de la lista incorporada de Python.
    """
    
    def __init__(self, iterable: Optional[List[T]] = None) -> None:
        """
        Inicializa una nueva lista doblemente enlazada.
        
        Args:
            iterable: Iterable opcional para inicializar la lista
        """
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self._size = 0
        
        if iterable:
            for item in iterable:
                self.append(item)
    
    def __len__(self) -> int:
        """Devuelve el número de elementos en la lista."""
        return self._size
    
    def __iter__(self) -> Iterator[T]:
        """Devuelve un iterador sobre los valores de la lista."""
        current = self.head
        while current:
            yield current.value
            current = current.next
    
    def __getitem__(self, index: int) -> T:
        """
        Obtiene el elemento en el índice especificado.
        
        Args:
            index: El índice del elemento a obtener
            
        Returns:
            El valor en el índice especificado
            
        Raises:
            IndexError: Si el índice está fuera de rango
        """
        if index < 0:
            index = self._size + index
        
        if index < 0 or index >= self._size:
            raise IndexError("Índice fuera de rango")
        
        # Determinar si comenzar desde la cabeza o la cola en función de cuál está más cerca
        if index < self._size // 2:
            # Comenzar desde la cabeza
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            # Comenzar desde la cola
            current = self.tail
            for _ in range(self._size - 1 - index):
                current = current.prev
        
        return current.value
    
    def __setitem__(self, index: int, value: T) -> None:
        """
        Establece el elemento en el índice especificado.
        
        Args:
            index: El índice del elemento a establecer
            value: El nuevo valor
            
        Raises:
            IndexError: Si el índice está fuera de rango
        """
        if index < 0:
            index = self._size + index
        
        if index < 0 or index >= self._size:
            raise IndexError("Índice fuera de rango")
        
        # Determinar si comenzar desde la cabeza o la cola en función de cuál está más cerca
        if index < self._size // 2:
            # Comenzar desde la cabeza
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            # Comenzar desde la cola
            current = self.tail
            for _ in range(self._size - 1 - index):
                current = current.prev
        
        current.value = value
    
    def __str__(self) -> str:
        """Devuelve una representación en cadena de la lista."""
        return str(list(self))
    
    def __repr__(self) -> str:
        """Devuelve una representación en cadena de la lista."""
        return f"DoublyLinkedList({list(self)})"
    
    def __eq__(self, other: Any) -> bool:
        """
        Comprueba si esta lista es igual a otro objeto.
        
        Args:
            other: El objeto con el que comparar
            
        Returns:
            True si las listas son iguales, False en caso contrario
        """
        if isinstance(other, DoublyLinkedList):
            return list(self) == list(other)
        elif isinstance(other, list):
            return list(self) == other
        return False
    
    def append(self, value: T) -> None:
        """
        Añade un valor al final de la lista.
        
        Args:
            value: El valor a añadir
        """
        new_node = Node(value)
        
        if not self.head:
            # La lista está vacía
            self.head = new_node
            self.tail = new_node
        else:
            # La lista no está vacía
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: T) -> None:
        """
        Añade un valor al principio de la lista.
        
        Args:
            value: El valor a añadir al principio
        """
        new_node = Node(value)
        
        if not self.head:
            # La lista está vacía
            self.head = new_node
            self.tail = new_node
        else:
            # La lista no está vacía
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self._size += 1
    
    def insert(self, index: int, value: T) -> None:
        """
        Inserta un valor en el índice especificado.
        
        Args:
            index: El índice donde insertar
            value: El valor a insertar
            
        Raises:
            IndexError: Si el índice está fuera de rango
        """
        if index < 0:
            index = self._size + index
        
        if index < 0 or index > self._size:
            raise IndexError("Índice fuera de rango")
        
        if index == 0:
            self.prepend(value)
        elif index == self._size:
            self.append(value)
        else:
            # Encontrar el nodo en el índice
            current = self.head
            for _ in range(index):
                current = current.next
            
            # Crear un nuevo nodo e insertarlo antes del actual
            new_node = Node(value)
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            
            self._size += 1
    
    def remove(self, value: T) -> None:
        """
        Elimina la primera ocurrencia de un valor de la lista.
        
        Args:
            value: El valor a eliminar
            
        Raises:
            ValueError: Si el valor no se encuentra
        """
        current = self.head
        
        while current:
            if current.value == value:
                self._remove_node(current)
                return
            current = current.next
        
        raise ValueError(f"Valor {value} no encontrado en la lista")
    
    def pop(self, index: int = -1) -> T:
        """
        Elimina y devuelve el elemento en el índice especificado.
        
        Args:
            index: El índice del elemento a eliminar (por defecto: -1, el último elemento)
            
        Returns:
            El valor del elemento eliminado
            
        Raises:
            IndexError: Si el índice está fuera de rango
        """
        if index < 0:
            index = self._size + index
        
        if index < 0 or index >= self._size:
            raise IndexError("Índice fuera de rango")
        
        node = self._get_node(index)
        value = node.value
        self._remove_node(node)
        
        return value
    
    def _remove_node(self, node: Node[T]) -> None:
        """
        Elimina un nodo de la lista.
        
        Args:
            node: El nodo a eliminar
        """
        if node.prev:
            node.prev.next = node.next
        else:
            # El nodo es la cabeza
            self.head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            # El nodo es la cola
            self.tail = node.prev
        
        self._size -= 1
    
    def index(self, value: T) -> int:
        """
        Devuelve el índice de la primera ocurrencia del valor.
        
        Args:
            value: El valor a buscar
            
        Returns:
            El índice del valor
            
        Raises:
            ValueError: Si el valor no se encuentra
        """
        current = self.head
        index = 0
        
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        
        raise ValueError(f"Valor {value} no encontrado en la lista")
    
    def clear(self) -> None:
        """Elimina todos los elementos de la lista."""
        self.head = None
        self.tail = None
        self._size = 0
    
    def copy(self) -> 'DoublyLinkedList[T]':
        """
        Crea una copia superficial de la lista.
        
        Returns:
            Una nueva lista con los mismos valores
        """
        return DoublyLinkedList(list(self))
    
    def swap(self, i: int, j: int) -> None:
        """
        Intercambia los valores en los índices i y j.
        
        Args:
            i: El primer índice
            j: El segundo índice
            
        Raises:
            IndexError: Si alguno de los índices está fuera de rango
        """
        if i < 0:
            i = self._size + i
        if j < 0:
            j = self._size + j
        
        if i < 0 or i >= self._size or j < 0 or j >= self._size:
            raise IndexError("Índice fuera de rango")
        
        if i == j:
            return
        
        # Obtener los nodos en los índices i y j
        node_i = self._get_node(i)
        node_j = self._get_node(j)
        
        # Intercambiar los valores
        node_i.value, node_j.value = node_j.value, node_i.value
    
    def _get_node(self, index: int) -> Node[T]:
        """
        Obtiene el nodo en el índice especificado.
        
        Args:
            index: El índice del nodo a obtener
            
        Returns:
            El nodo en el índice especificado
            
        Raises:
            IndexError: Si el índice está fuera de rango
        """
        if index < 0:
            index = self._size + index
        
        if index < 0 or index >= self._size:
            raise IndexError("Índice fuera de rango")
        
        # Determinar si comenzar desde la cabeza o la cola en función de cuál está más cerca
        if index < self._size // 2:
            # Comenzar desde la cabeza
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            # Comenzar desde la cola
            current = self.tail
            for _ in range(self._size - 1 - index):
                current = current.prev
        
        return current
    
    def to_list(self) -> List[T]:
        """
        Convierte la lista enlazada a una lista de Python.
        
        Returns:
            Una lista con los valores de la lista enlazada
        """
        return list(self)
    
    @classmethod
    def from_list(cls, lst: List[T]) -> 'DoublyLinkedList[T]':
        """
        Crea una nueva DoublyLinkedList a partir de una lista de Python.
        
        Args:
            lst: La lista a convertir
            
        Returns:
            Una nueva DoublyLinkedList con los valores de la lista
        """
        return cls(lst)


def adapt_sort_algorithm(sort_func: Callable) -> Callable:
    """
    Adapta una función de ordenación para que funcione con DoublyLinkedList.
    
    Args:
        sort_func: La función de ordenación a adaptar
        
    Returns:
        Una nueva función que puede ordenar DoublyLinkedList
    """
    @functools.wraps(sort_func)
    def wrapper(data: Union[List[int], DoublyLinkedList[int]], trace: bool = False) -> Union[
        DoublyLinkedList[int], Generator[DoublyLinkedList[int], None, DoublyLinkedList[int]]
    ]:
        if isinstance(data, DoublyLinkedList):
            if trace:
                # Si el seguimiento está habilitado, generar estados intermedios
                steps = []
                
                # Convertir a lista, ordenar con seguimiento y convertir los pasos de nuevo a DoublyLinkedList
                data_list = data.to_list()
                for step in sort_func(data_list, trace=True):
                    steps.append(DoublyLinkedList(step))
                
                # Devolver un generador para los pasos
                for step in steps:
                    yield step
                
                return steps[-1]
            else:
                # Si el seguimiento está desactivado, simplemente ordenar y devolver
                data_list = data.to_list()
                result_list = sort_func(data_list, trace=False)
                return DoublyLinkedList(result_list)
        else:
            # Si no es DoublyLinkedList, pasar a la función original
            return sort_func(data, trace)
    
    return wrapper


# Diccionario para almacenar algoritmos de ordenación adaptados para listas enlazadas
_LINKED_LIST_ALGORITHMS: Dict[str, Callable] = {}


def register_linked_list_algorithm(name: str, algorithm: Callable) -> None:
    """
    Registra un algoritmo de ordenación para su uso con DoublyLinkedList.
    
    Args:
        name: El nombre del algoritmo
        algorithm: La función del algoritmo a registrar
    """
    _LINKED_LIST_ALGORITHMS[name] = adapt_sort_algorithm(algorithm)


def get_linked_list_algorithm(name: str) -> Callable:
    """
    Obtiene un algoritmo de ordenación registrado por su nombre.
    
    Args:
        name: El nombre del algoritmo
        
    Returns:
        La función del algoritmo
        
    Raises:
        ValueError: Si el algoritmo no está registrado
    """
    if name not in _LINKED_LIST_ALGORITHMS:
        valid_names = list(_LINKED_LIST_ALGORITHMS.keys())
        raise ValueError(f"Algoritmo de lista enlazada no registrado: {name}. Algoritmos registrados: {valid_names}")
    
    return _LINKED_LIST_ALGORITHMS[name]


def list_linked_list_algorithms() -> List[str]:
    """
    Lista todos los algoritmos de ordenación de listas enlazadas registrados.
    
    Returns:
        Una lista de nombres de algoritmos registrados
    """
    return list(_LINKED_LIST_ALGORITHMS.keys())
