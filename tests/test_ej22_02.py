import pytest 
from src.Bucles.ej22_02 import comprobar_si_num,años_cumplidos
@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("5", 5),
        ("4", 4),
    ]
)
def test_comprobar_si_num(input_x,expected):
    assert comprobar_si_num(input_x)== expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (5,"1,2,3,4,5."),
        (4,"1,2,3,4."),
    ]
)
def test_años_cumplidos(input_x,expected):
    assert años_cumplidos(input_x)== expected