# Pruebas de Algoritmos de Búsqueda

Este directorio contiene pruebas unitarias para el paquete de algoritmos de búsqueda.

## Archivos de Prueba

- `test_linear_search.py`: Pruebas para el algoritmo de búsqueda lineal
- `test_binary_search.py`: Pruebas para el algoritmo de búsqueda binaria
- `test_exponential_search.py`: Pruebas para el algoritmo de búsqueda exponencial
- `test_interpolation_search.py`: Pruebas para el algoritmo de búsqueda por interpolación
- `test_factory.py`: Pruebas para la factoría de algoritmos de búsqueda
- `test_performance.py`: Pruebas que comparan el rendimiento de diferentes algoritmos

## Ejecutar Pruebas

Puedes ejecutar todas las pruebas con:

```bash
python -m search_algorithms.tests.run_tests
```

O ejecutar archivos de prueba individuales:

```bash
python -m unittest search_algorithms.tests.test_linear_search
```

## Cobertura de Pruebas

Las pruebas cubren:

1. **Corrección**: Verificar que cada algoritmo encuentra correctamente elementos en arrays
2. **Casos Límite**: Probar comportamiento con arrays vacíos, arrays de un solo elemento, etc.
3. **Rendimiento**: Comparar la eficiencia de diferentes algoritmos
4. **Patrón Factoría**: Probar la creación y registro de algoritmos

## Añadir Nuevas Pruebas

Al añadir un nuevo algoritmo de búsqueda, por favor crea un archivo de prueba correspondiente
siguiendo el patrón existente. Asegúrate de que tus pruebas cubran al menos:

- Encontrar elementos al principio, medio y final de los arrays
- Manejar casos límite (array vacío, elemento no encontrado)
- Verificar la funcionalidad de conteo de iteraciones
- Probar cualquier característica específica del algoritmo
