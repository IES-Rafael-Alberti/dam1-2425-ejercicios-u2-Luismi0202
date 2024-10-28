import pytest 
from src.Bucles.ej22_05 import capital_obtenido 

@pytest.mark.parametrize(
    "input_x,input_y,input_z,expected",
    [
        (8,100,1,"En 1 año obtendrá un capital de: 16.00€"),
    ]
)
def test_capital_obtenido(input_x,input_y,input_z,expected):
    assert capital_obtenido(input_x,input_y,input_z)==expected