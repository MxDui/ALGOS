from typing import List, Optional, Iterator, TypeVar, Generic, Any, Union, Callable, Dict, Generator, Iterable
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
            new_node = Node(value)
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            self._size += 1
    
    def remove(self, value: T) -> None:
        """
        Elimina la primera ocurrencia del valor.
        
        Args:
            value: El valor a eliminar
            
        Raises:
            ValueError: Si el valor no se encuentra en la lista
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
            index: El índice del elemento a eliminar (por defecto, el último)
            
        Returns:
            El valor eliminado
            
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
        # Actualizar referencias a prev y next
        if node.prev:
            node.prev.next = node.next
        else:
            # Nodo es la cabeza
            self.head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            # Nodo es la cola
            self.tail = node.prev
        
        self._size -= 1
    
    def index(self, value: T) -> int:
        """
        Devuelve el índice del primer elemento con el valor especificado.
        
        Args:
            value: El valor a buscar
            
        Returns:
            El índice del elemento encontrado
            
        Raises:
            ValueError: Si el valor no se encuentra en la lista
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
            i: Primer índice
            j: Segundo índice
            
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
        
        # Obtener los nodos
        node_i = self._get_node(i)
        node_j = self._get_node(j)
        
        # Intercambiar valores
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
        Convierte la lista enlazada a una lista Python.
        
        Returns:
            Una lista Python con los mismos valores que la lista enlazada
        """
        return list(self)
    
    @classmethod
    def from_list(cls, lst: List[T]) -> 'DoublyLinkedList[T]':
        """
        Crea una lista enlazada a partir de una lista Python.
        
        Args:
            lst: La lista Python a convertir
            
        Returns:
            Una nueva lista enlazada con los mismos valores que la lista Python
        """
        return cls(lst)


def adapt_sort_algorithm(sort_func: Callable) -> Callable:
    """
    Adapta una función de ordenación para trabajar con DoublyLinkedList.
    
    Args:
        sort_func: La función de ordenación original que opera en listas
        
    Returns:
        Una nueva función que soporta DoublyLinkedList
    """
    
    @functools.wraps(sort_func)
    def wrapper(data: Union[List[int], DoublyLinkedList[int]], trace: bool = False) -> Union[
        DoublyLinkedList[int], Generator[DoublyLinkedList[int], None, DoublyLinkedList[int]]
    ]:
        """
        Envoltorio para ordenar una DoublyLinkedList utilizando una función de ordenación de lista.
        
        Args:
            data: La DoublyLinkedList a ordenar
            trace: Si se deben generar estados intermedios
            
        Returns:
            Si trace es False, la DoublyLinkedList ordenada
            Si trace es True, un generador que produce estados intermedios como DoublyLinkedList
        """
        # Convertir a lista
        lst = data.to_list() if isinstance(data, DoublyLinkedList) else data
        
        if trace:
            # Ejecutar con seguimiento y convertir cada paso a DoublyLinkedList
            steps_generator = sort_func(lst, trace=True)
            for step in steps_generator:
                yield DoublyLinkedList(step)
        else:
            # Ejecutar sin seguimiento y convertir el resultado a DoublyLinkedList
            result = sort_func(lst, trace=False)
            return DoublyLinkedList(result)
    
    return wrapper


# Diccionario para algoritmos adaptados
LINKED_LIST_ALGORITHMS: Dict[str, Callable] = {}


def register_linked_list_algorithm(name: str, algorithm: Callable) -> None:
    """
    Registra una función de ordenación adaptada para DoublyLinkedList.
    
    Args:
        name: El nombre del algoritmo
        algorithm: La función de ordenación original
    """
    LINKED_LIST_ALGORITHMS[name] = adapt_sort_algorithm(algorithm)


def get_linked_list_algorithm(name: str) -> Callable:
    """
    Obtiene una función de ordenación adaptada para DoublyLinkedList por su nombre.
    
    Args:
        name: El nombre del algoritmo
        
    Returns:
        La función de ordenación adaptada
        
    Raises:
        ValueError: Si el nombre del algoritmo no está registrado
    """
    if name not in LINKED_LIST_ALGORITHMS:
        valid_names = list(LINKED_LIST_ALGORITHMS.keys())
        raise ValueError(f"Algoritmo de lista enlazada desconocido: {name}. Las opciones válidas son: {valid_names}")
    
    return LINKED_LIST_ALGORITHMS[name]


def list_linked_list_algorithms() -> List[str]:
    """
    Lista todos los nombres de algoritmos adaptados para DoublyLinkedList disponibles.
    
    Returns:
        Una lista de nombres de algoritmos adaptados
    """
    return list(LINKED_LIST_ALGORITHMS.keys()) 