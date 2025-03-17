# Algoritmos de Búsqueda en Arreglos

Este programa implementa cuatro algoritmos de búsqueda en arreglos ordenados:

1. Búsqueda Lineal
2. Búsqueda Binaria
3. Búsqueda Exponencial
4. Búsqueda por Interpolación

## Requisitos

- Python 3.x
- Matplotlib (opcional, para la comparación de rendimiento)

## Estructura del Proyecto

- `search_algorithms.py`: Implementación básica de los algoritmos
- `search_interactive.py`: Versión interactiva que permite al usuario ingresar datos
- `performance_comparison.py`: Comparación de rendimiento entre algoritmos
- `logger_config.py`: Configuración centralizada del sistema de logging

## Sistema de Logging

El proyecto utiliza el módulo `logging` de Python para mostrar información durante la ejecución:

- Los mensajes informativos se muestran en la consola
- En el caso de la comparación de rendimiento, también se guardan en un archivo `performance_results.log`
- Se utilizan diferentes niveles de logging (INFO, WARNING, ERROR)

## Ejecución

Hay tres versiones del programa:

### Versión con datos predefinidos

```bash
python search_algorithms.py
```

Esta versión ejecuta los algoritmos con un arreglo predefinido y muestra los resultados.

### Versión interactiva

```bash
python search_interactive.py
```

Esta versión permite al usuario:

- Ingresar su propio arreglo
- Verificar si el arreglo está ordenado (y ordenarlo si es necesario)
- Ingresar el elemento a buscar
- Realizar múltiples búsquedas

### Comparación de rendimiento

```bash
python performance_comparison.py
```

Esta versión:

- Compara el rendimiento de los cuatro algoritmos con diferentes tamaños de arreglos
- Mide el tiempo de ejecución promedio para cada algoritmo
- Genera una gráfica comparativa (requiere matplotlib)
- Guarda la gráfica como 'performance_comparison.png'
- Registra los resultados en 'performance_results.log'

Para instalar matplotlib:

```bash
pip install matplotlib
```

## Descripción de los Algoritmos

### Búsqueda Lineal

- **Precondiciones**: El arreglo puede estar ordenado o no.
- **Complejidad**: O(n) en tiempo, O(1) en espacio.
- **Funcionamiento**: Recorre el arreglo elemento por elemento hasta encontrar el valor buscado.

### Búsqueda Binaria

- **Precondiciones**: El arreglo debe estar ordenado.
- **Complejidad**: O(log n) en tiempo, O(1) en espacio.
- **Funcionamiento**: Divide repetidamente el arreglo a la mitad, descartando la mitad donde no puede estar el elemento.

### Búsqueda Exponencial

- **Precondiciones**: El arreglo debe estar ordenado.
- **Complejidad**: O(log n) en tiempo, O(1) en espacio.
- **Funcionamiento**: Encuentra un rango donde podría estar el elemento mediante saltos exponenciales, luego aplica búsqueda binaria en ese rango.

### Búsqueda por Interpolación

- **Precondiciones**: El arreglo debe estar ordenado y los elementos deben estar uniformemente distribuidos.
- **Complejidad**: O(log log n) en el caso promedio, O(n) en el peor caso.
- **Funcionamiento**: Estima la posición del elemento basándose en su valor y los valores en los extremos del arreglo.

## Salida

El programa muestra cada iteración realizada por los algoritmos, incluyendo:

- Los índices y valores que se están comparando
- El resultado final (índice donde se encontró el elemento o -1 si no existe)

Se ejecutan dos casos de prueba:

1. Búsqueda de un elemento que existe en el arreglo
2. Búsqueda de un elemento que no existe en el arreglo
