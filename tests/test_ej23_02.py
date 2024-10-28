import pytest 
from src.Excepciones.ej23_02 import mostrar_impares

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (25, "IMPARES=>1,3,5,7,9,11,13,15,17,19,21,23,25."),
        (8, "IMPARES=>1,3,5,7.")
    ]
)   
def test_mostrar_impares(input_x,expected):
    assert mostrar_impares(input_x)== expected