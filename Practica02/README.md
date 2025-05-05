# Practica02: Kit Modular de Algoritmos de Ordenamiento

Un paquete Python modular que implementa y analiza algoritmos clásicos de ordenamiento. Este kit proporciona implementaciones de los algoritmos de ordenamiento selection sort, insertion sort, quick sort, heap sort y merge sort. 

## Características

- Cinco algoritmos de ordenamiento con capacidad de seguimiento
- Demostración automática de todos los algoritmos con la visualización de los pasos
- Utilidades de evaluación comparativa para comparar el rendimiento de los algoritmos
- Implementación de lista doblemente ligada con los mismos algoritmos

## Instalación

```bash
# Instalar en modo desarrollo
pip install -e .

# Instalar con dependencias de desarrollo
pip install -e ".[dev]"
```

## Uso

### Ejecución de la Demostración

```bash
# Ejecutar la demostración automática de todos los algoritmos
python -m practica02
```

Al ejecutar el módulo, se mostrará automáticamente:

- Una demostración de todos los algoritmos usando implementación de array
- Una demostración de todos los algoritmos usando implementación de lista enlazada
- Visualización paso a paso del proceso de ordenamiento
- Medición del tiempo de ejecución para cada algoritmo

### API de Python

```python
from practica02 import quick_sort, merge_sort

# Ordenamiento básico
sorted_list = quick_sort([3, 1, 4, 1, 5, 9, 2, 6])

# Obtener trazas intermedias
for step in quick_sort([3, 1, 4, 1, 5, 9, 2, 6], trace=True):
    print(step)
```

## Complejidad de Algoritmos

| Algoritmo                  | Tiempo (Mejor) | Tiempo (Promedio) | Tiempo (Peor) | Espacio  | Estable |
| -------------------------- | -------------- | ----------------- | ------------- | -------- | ------- |
| Ordenamiento por Selección | O(n²)          | O(n²)             | O(n²)         | O(1)     | No      |
| Ordenamiento por Inserción | O(n)           | O(n²)             | O(n²)         | O(1)     | Sí      |
| Ordenamiento Rápido        | O(n log n)     | O(n log n)        | O(n²)         | O(log n) | No      |
| Ordenamiento Merge         | O(n log n)     | O(n log n)        | O(n log n)    | O(n)     | Sí      |
| Ordenamiento Heap          | O(n log n)     | O(n log n)        | O(n log n)    | O(1)     | No      |

## Autor

David Rivera Morales y José Antonio Gallegos Cortes
