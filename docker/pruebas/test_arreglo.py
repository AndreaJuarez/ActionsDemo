import pytest
import arreglo as arreglo

array = [5,3,4,2,1]
diccionario = [{"nombre":"Eduardo","edad":23},
               {"nombre":"Melissa","edad":7},
               {"nombre":"Andrea","edad":21}]

def test_arreglo():
    assert arreglo.order(array) == [1,2,3,4,5]

def test_count_mayor():
    assert arreglo.count_mayor(diccionario) == 2