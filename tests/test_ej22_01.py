import pytest 
from src.Bucles.ej22_01 import repetir_palabra
@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("HOLA","HOLA"),
        ("JUAN","JUAN"),
    ]
)
def test_repetir_palabra(input_x,expected):
    assert repetir_palabra(input_x)==expected