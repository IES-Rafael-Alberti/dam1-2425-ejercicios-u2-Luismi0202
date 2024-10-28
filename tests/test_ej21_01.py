import pytest 
from src.Condicionales.ej21_01 import si_negativo,si_decimal,comprobar_si_num,mayor_de_edad
@pytest.mark.parametrize(
    "input_x,expected",
    [
        (5,5),
        (10,10),
        (15,15)
    ]
)

def test_si_negativo(input_x,expected):
    assert si_negativo(input_x)==expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        (4.5,True),
        (4,False),
        (7.6,True)
    ]
)
def test_si_decimal(input_x,expected):
    assert si_decimal(input_x)==expected
@pytest.mark.parametrize(
    "input_x,expected",
    [
        (4,True),
        ("a",False),
        (7,True)
    ]
)
def test_si_num(input_x,expected):
    assert comprobar_si_num(input_x)==expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        (4, "lo siento eres menor adiós *se va*"),
        (18, "¡¡PERFECTO, ERES MAYOR DE EDAD!!¡¡VAMONOS A POR CERVEZA!!"),
    ]
)
def test_mayor(input_x,expected):
    assert mayor_de_edad(input_x)==expected