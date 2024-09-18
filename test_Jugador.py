import pytest
from Jugador import Jugador
def test_constructor():
   j =Jugador("Adrian",6)
   assert(j.nombre == "Adrian")
   assert(j.fichas ==6)

def test_constructor_sin_fichas():
   j =Jugador("Adrian")
   assert(j.nombre == "Adrian")
   assert(j.fichas == 5)

def test_dar_fichas():
   j = Jugador("Adrian", 10)
   j.darFicha(5)
   assert(j.fichas ==15)

def test_dar_fichas_sin_fichas():
   j = Jugador("Adrian")
   j.darFicha()
   assert(j.fichas == 6)

def test_sacar_fichas():
   j = Jugador("Adrian",10)
   j.sacarFicha(5)
   assert(j.fichas == 5)

def test_entregar_fichas_sin_fichas():
   j = Jugador("Adrian",10)
   j.sacarFicha()
   assert(j.fichas == 9)

def test_sacar_fichas_demás():
   j = Jugador("Adrian",10)
   with pytest.raises(ValueError):
    j.sacarFicha(11)

def test_no_tiene_fichas():
    j = Jugador("Adrian", 10)
    j.sacarFicha(10)
    assert j.sinFichas()  

def test_tiene_fichas():
    j = Jugador("Adrian", 5)
    j.sacarFicha(4)
    assert not j.sinFichas()  
