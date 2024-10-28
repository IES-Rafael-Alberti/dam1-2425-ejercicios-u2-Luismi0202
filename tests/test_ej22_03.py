import pytest 
from src.Bucles.ej22_03 import comprobar_num,num_impares
@pytest.mark.parametrize(
    "input_x,expected",
    [
        (8, True),
        (-5, False),
    ]
)
def test_comprobar_num(input_x,expected):
   assert comprobar_num(input_x)== expected

@pytest.mark.parametrize(
    "input_x,expected",
    [
        (8,"1,3,5,7,8."),
        (5,"1,3,5.")
    ]
)
def test_num_impares(input_x,expected):
   assert num_impares(input_x)==expected