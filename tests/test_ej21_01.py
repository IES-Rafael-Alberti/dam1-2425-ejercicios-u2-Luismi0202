import pytest 
from src.Condicionales.ej21_01 import si_negativo,si_decimal,comprobar_si_num,mayor_de_edad

def test_si_negativo():
    assert si_negativo(5)==5
def test_si_decimal():
    assert si_decimal(4.5)== True
def test_si_num():
    assert comprobar_si_num(4.5)== True