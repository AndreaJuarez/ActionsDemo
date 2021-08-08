import pytest
import arreglo as ar

array = [5,3,4,2,1]
diccionario = [
    {"nombre":"Eduardo","edad":23},
    {"nombre":"Melissa","edad":7},
    {"nombre":"Andrea","edad":21}]

def test_arreglo():
    assert ar.order(array) == [1,2,3,4,5]

def test_contar_mayores():
    assert ar.count_mayores(diccionario) == 2