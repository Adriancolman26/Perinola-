from perinola import Perinola
from apuestas import Apuesta
from jugador import Jugador
from ronda import Ronda


#p = Perinola()
#p.tirar()
#print(p.cara_visible)

#A = Apuesta()
#print(A)

#J = Jugador("Adrián, 26")
#print(J)

jugador1 = Jugador("Tomás", 15)
jugador2 = Jugador("Andrés", 5)
jugador3 = Jugador("Lucía", 0)
jugador4 = Jugador("Marta", 10)

ronda = Ronda()

ronda.agregarJugador(jugador1)
ronda.agregarJugador(jugador2)

try:
    ronda.agregarJugador(jugador3)
except ValueError as e:
    print(e)

ronda.agregarJugador(jugador4)

print("Estado inicial de la ronda:")
print(ronda)

ronda.pasarTurno()
print("\nDespués de pasar el turno:")
print(ronda) 

print("\nJugador en turno:")
print(ronda.jugadorEnTurno()) 

ronda.sacarJugadoresSinFichas()
print("\nDespués de eliminar jugadores sin fichas:")
print(ronda) 

if ronda.quedaUnSoloJugador():
    print("\nQueda un solo jugador en la ronda.")
else:
    print("\nQuedan varios jugadores en la ronda.")

