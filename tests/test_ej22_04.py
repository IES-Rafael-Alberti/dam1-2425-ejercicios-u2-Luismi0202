import pytest 
from src.Bucles.ej22_04 import comprobar_num,cuenta_atras

def test_comprobar_num():
    assert comprobar_num(8)== True
def test_cuenta_atras():
    assert cuenta_atras(8)== "8,7,6,5,4,3,2,1,0."