import pytest 
from src.Excepciones.ej23_03 import cuenta_atras

def test_cuenta_atras():
    assert cuenta_atras(8)=="CUENTA ATRÁS=>8...7...6...5...4...3...2...1...0...¡DESPEGUE!"
@pytest.mark.parametrize(
    "input_x,expected",
    [
        (8,"CUENTA ATRÁS=>8...7...6...5...4...3...2...1...0...¡DESPEGUE!"),
        (9,"CUENTA ATRÁS=>9...8...7...6...5...4...3...2...1...0...¡DESPEGUE!")
    ]
)   
def test_cuenta_atras(input_x,expected):
    assert cuenta_atras(input_x)==expected