import pytest 
from src.Excepciones.ej23_03 import cuenta_atras

def test_cuenta_atras():
    assert cuenta_atras(8)=="CUENTA ATRÁS=>8...7...6...5...4...3...2...1...0...¡DESPEGUE!"