import pytest 
from src.Bucles.ej22_20 import encontrar_letra

@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        ("a","a","Se encontró una coincidencia en el caracter a EN POSICIÓN 1 \n"),
    ]
)
def test_encontrar_letra(input_x,input_y,expected):
    assert encontrar_letra(input_x,input_y)==expected