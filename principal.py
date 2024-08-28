from perinola import Perinola
from apuestas import Apuesta

p = Perinola()
p.tirar()
print(p.cara_visible)


A = Apuesta()
A.tomarFichas(5)
print(A)