import pytest 
from src.Bucles.ej22_02 import comprobar_si_num,años_cumplidos

def test_comprobar_si_num():
    assert comprobar_si_num("5")== 5
def test_años_cumplidos():
    assert años_cumplidos(5)== "1,2,3,4,5."