import pytest 
from src.Condicionales.ej21_05 import comprobar_si_num,tributa 
@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("4",True),
        ("a",False),
    ]
)
def test_comprobar_si_num(input_x,expected):
    comprobar_si_num(input_x)==expected 

@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        (18,2000, "¡¡EHNORABUENA!! USTED TRIBUTA"),
        (16,5,"LO SENTIMOS, USTED NO TRIBUTAS"),
    ]
)
def test_tributa(input_x,input_y,expected):
    tributa(input_x,input_y)==expected 