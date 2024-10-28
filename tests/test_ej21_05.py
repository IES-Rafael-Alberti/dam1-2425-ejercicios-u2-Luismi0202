import pytest 
from src.Condicionales.ej21_05 import comprobar_si_num,tributa 

def test_comprobar_si_num():
    assert comprobar_si_num("4")== True
def test_tributa():
    assert tributa(18,2000)== "¡¡EHNORABUENA!! USTED TRIBUTA"