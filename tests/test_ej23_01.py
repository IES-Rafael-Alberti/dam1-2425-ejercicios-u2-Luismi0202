import pytest 
from src.Excepciones.ej23_01 import mostrar_años_cumplidos
@pytest.mark.parametrize(
    "input_x,expected",
    [
        (25,"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25."),
        (8,"1,2,3,4,5,6,7,8.")
    ]
)    

def test_mostrar_años_cumplidos(input_x,expected):
    assert mostrar_años_cumplidos(input_x)==expected