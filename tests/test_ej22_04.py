import pytest 
from src.Bucles.ej22_04 import comprobar_num,cuenta_atras
@pytest.mark.parametrize(
    "input_x,expected",
    [
        (8,True),
        (-5,False),
        ("a",False)
    ]
)
def test_comprobar_num(input_x,expected):
    assert comprobar_num(input_x)== expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (8, "8,7,6,5,4,3,2,1,0."),
        (7, "7,6,5,4,3,2,1,0."),
    ]
)
def test_cuenta_atras(input_x,expected):
    assert cuenta_atras(input_x)== expected