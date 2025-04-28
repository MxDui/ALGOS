import pytest
from typing import List

from practica02.core.base import BaseSorter


class TestBaseSorter:
    """Pruebas para el algoritmo de ordenamiento base."""

    def test_base_sorter_not_instantiable(self):
        """Comprobar que BaseSorter no se puede instanciar directamente."""
        with pytest.raises(TypeError):
            sorter = BaseSorter()

    def test_base_sorter_not_implemented(self):
        """Comprobar que sort_values levanta NotImplementedError."""
        with pytest.raises(NotImplementedError):
            # Intentamos llamar al método estático directamente sin instanciar
            BaseSorter.sort_values([1, 2, 3]) 