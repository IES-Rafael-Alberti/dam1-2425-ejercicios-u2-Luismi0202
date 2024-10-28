import pytest 
from src.Bucles.ej22_05 import capital_obtenido 

def test_capital_obtenido():
    assert capital_obtenido(8,100,1)=="En 1 año obtendrá un capital de: 16.00€"