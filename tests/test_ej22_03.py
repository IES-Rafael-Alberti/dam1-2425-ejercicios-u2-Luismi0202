import pytest 
from src.Bucles.ej22_03 import comprobar_num,num_impares

def test_comprobar_num():
   assert comprobar_num(8)== True
def test_num_impares():
   assert num_impares(8)=="1,3,5,7,8."