# Algoritmos de Búsqueda

Esta biblioteca proporciona implementaciones de varios algoritmos de búsqueda, junto con utilidades para probar, comparar y visualizar su rendimiento.

## Algoritmos Implementados

1. **Búsqueda Lineal**

   - Complejidad Temporal: O(n)
   - Complejidad Espacial: O(1)
   - Funciona en arreglos no ordenados

2. **Búsqueda Binaria**

   - Complejidad Temporal: O(log n)
   - Complejidad Espacial: O(1)
   - Requiere arreglos ordenados

3. **Búsqueda Exponencial**

   - Complejidad Temporal: O(log n)
   - Complejidad Espacial: O(1)
   - Requiere arreglos ordenados
   - Particularmente eficiente para arreglos no acotados

4. **Búsqueda por Interpolación**
   - Complejidad Temporal: O(log log n) caso promedio, O(n) peor caso
   - Complejidad Espacial: O(1)
   - Requiere arreglos ordenados
   - Funciona mejor con valores distribuidos uniformemente

## Estructura del Proyecto

```
search_algorithms/
├── algorithms/         # Implementaciones de algoritmos
│   ├── base.py         # Clase base de algoritmo de búsqueda
│   ├── linear.py       # Implementación de búsqueda lineal
│   ├── binary.py       # Implementación de búsqueda binaria
│   ├── exponential.py  # Implementación de búsqueda exponencial
│   ├── interpolation.py # Implementación de búsqueda por interpolación
│   └── factory.py      # Factoría para crear instancias de algoritmos
├── utils/              # Funciones de utilidad
│   ├── logger.py       # Utilidades de registro
│   └── performance.py  # Utilidades de medición de rendimiento
├── visualization/      # Utilidades de visualización
│   └── performance_plots.py # Utilidades de graficación de rendimiento
└── tests/              # Pruebas unitarias
```

### Uso Básico

Basta con tener los requisitos especificados más abajo para poder ejecutar el programa. Una vez se tengan los requisitos instalados simplemente deben abrir la carpeta algorithms desde la terminal y escribir lo siguiente:
      python main.py
Esto debe de comenzar dos ejecuciones del programa, una es la busqueda del número 7 en un arreglo predefinido, mientras que la otra es la busqueda del número 2 en ese mismo arreglo para ver como se comportan las funciones cuándo el número no se encuentra en el arreglo dado.

Además hay un archivo llamado "otros", el cuál permite hacer la ejecución de cualquier algoritmo de busqueda implementado con cuálquier arreglo, para esto deben de ir a la misma carpeta algorithms donde se encuentra el main y escribir el siguiente comando en la terminal:
      python otros.py exponential 11 --data 1 3 5 7 9 11
Este está conformado por 3 cosas que pueden variar 3
     python otros.py _algoritmo_ _target_ --data _ARREGLO SEPARADO CON ESPACIOS_
En _algoritmo_ pueden poner "binary", "linear", "exponential" e "interpolation".
En _target_ pueden poner cualquier número entero
En _ARREGLO SEPARADO CON ESPACIOS_ pueden poner cualquier "lista" de números siempre y cuándo esté separada con espacios.

Cabe resaltar que el archivo main.py genera una gráfica de las iteraciones que se hicieron en la ejecución, estas gráficas las pueden encontrar en la carpeta "plots" que debería de generarse una vez ejecuten el main. El archivo otros.py no genera estas gráficas, solo lo muestra en la terminal.



```python
from search_algorithms.algorithms import SearchAlgorithmFactory
from search_algorithms.utils import get_console_logger

# Crear un logger
logger = get_console_logger("search_demo")

# Obtener una instancia de algoritmo de búsqueda
binary_search = SearchAlgorithmFactory.get_algorithm("binary", logger)

# Buscar un elemento
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search.search(arr, target)

print(f"Elemento encontrado en el índice: {result}")
print(f"Número de iteraciones: {binary_search.iterations}")
```

### Uso de Todos los Algoritmos

```python
from search_algorithms.algorithms import SearchAlgorithmFactory
from search_algorithms.utils import get_console_logger

# Crear un logger
logger = get_console_logger("search_demo")

# Obtener todos los algoritmos de búsqueda
algorithms = SearchAlgorithmFactory.get_all_algorithms(logger)

# Arreglo en el que buscar
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

# Ejecutar cada algoritmo e imprimir resultados
for name, algorithm in algorithms.items():
    result = algorithm.search(arr, target)
    print(f"{algorithm.name}: Encontrado en el índice {result}, iteraciones: {algorithm.iterations}")
```

### Pruebas de Rendimiento

```python
from search_algorithms.algorithms import SearchAlgorithmFactory
from search_algorithms.utils import run_performance_test
from search_algorithms.visualization import save_plots

# Obtener todos los algoritmos sin logging
algorithms = SearchAlgorithmFactory.get_all_algorithms()

# Ejecutar pruebas de rendimiento
sizes = [100, 1000, 10000, 100000]
results = run_performance_test(algorithms, sizes)

# Guardar gráficas
save_plots(results, output_dir="plots")
```

## Herramientas de Línea de Comandos

El proyecto incluye dos scripts de línea de comandos:

1. **interactive_search.py**: Interfaz interactiva para probar algoritmos de búsqueda

   ```
   python interactive_search.py
   ```

2. **performance_test.py**: Ejecutar pruebas de rendimiento y generar visualizaciones

   ```
   python performance_test.py

   # Para pruebas extendidas con arreglos más grandes
   python performance_test.py --extended
   ```

## Patrones de Diseño Utilizados

1. **Patrón Factoría**: La clase `SearchAlgorithmFactory` maneja la creación de instancias de algoritmos
2. **Patrón Estrategia**: Cada algoritmo de búsqueda es una implementación concreta de la clase base abstracta `SearchAlgorithm`
3. **Patrón Método Plantilla**: La clase base define el esqueleto de operaciones, permitiendo a las subclases implementar pasos específicos

## Dependencias

- Python 3.6+
- matplotlib (para visualización)

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/yourusername/search-algorithms.git
cd search-algorithms

# Instalar dependencias
pip install -r requirements.txt
```

## Licencia

Licencia MIT
