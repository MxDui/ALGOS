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
│   └── factory.py      # Fabrica que crea instancias de algoritmos
├── utils/              # Funciones de utilidad
│   ├── logger.py       # Utilidades de registro
│   └── performance.py  # Utilidades de medición de rendimiento
├── tests/              # Pruebas unitarias
└── main.py             # Archivo main que ejecuta una prueba para cada algoritmo

```

### Uso Básico

Basta con tener los requisitos especificados más abajo para poder ejecutar el programa. Una vez se tengan los requisitos instalados simplemente deben abrir la carpeta raíz (practica01) desde la terminal y escribir lo siguiente:
python main.py
Esto debe de comenzar la busqueda de la mitad de un arreglo ordenado de 10, 100, 500 y 1000 elementos, además de que hace otra busqueda en ese mismo arreglo pero ahora con un número que no aparece en el arreglo para ver como se comportan las funciones cuándo el número no se encuentra en el arreglo dado. Hicimos además pruebas unitarias, en la carpeta test hay un readme con más información.

## Dependencias

- Python 3.6+
- colorama (para colores en la terminal)

## Instalación

```bash
Deben estar en la carpeta practica01

# Instalar dependencias en caso de faltar
pip install -r requirements.txt
```

## Licencia

Licencia MIT
