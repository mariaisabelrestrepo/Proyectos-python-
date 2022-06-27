'''import random 
def tiene_cartas_altas(cartas_siguientes):
    
    # ACÁ INICIA LA FUNCIÓN
    for i in cartas_siguientes:
        if i in 'AJQK':
            return True
    return False
    # ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS  
def juego(baraja):
    # ACÁ INICIA LA FUNCIÓN
    random.shuffle(baraja)
    num_cartas=len(baraja)
    jugador='jugador_1'
    puntaje_jugador1=0
    puntaje_jugador2=0
    for i,j in enumerate(baraja):
        puntos=0
        total_cartas=num_cartas-i-1
       
        if j=='A' and total_cartas>=1 and not(tiene_cartas_altas(baraja[i+1])):
            puntos=1
        elif j=='J'and total_cartas>=2 and not(tiene_cartas_altas(baraja[i+1:i+3])):
            puntos=2
        elif j=='Q'and total_cartas>=3 and not(tiene_cartas_altas(baraja[i+1:i+4])):
            puntos=3
        elif j=='K'and total_cartas>=4 and not(tiene_cartas_altas(baraja[i+1:i+5])):
            puntos=4
        if jugador=="jugador_1":
            puntaje_jugador1+=puntos
            jugador='jugador_2'
             
        else:
            puntaje_jugador2+=puntos
            jugador='jugador_1'
    print(puntaje_jugador1,puntaje_jugador2)
    return puntaje_jugador1, puntaje_jugador2

    # ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS
    
juego(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'Q', 'K']*4)


'''
# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN
import random
def tiene_cartas_altas(cartas_siguientes):
    # ACÁ INICIA LA FUNCIÓN
    for c in cartas_siguientes:
        if c in "AJQK":
           return True
    return False
# ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS

def juego(baraja):
  random.shuffle(baraja)
  puntaje_jugador1 = 0
  puntaje_jugador2 = 0
  puntaje_jugador ="jugador1"
  puntaje_actual = 0
  
  for i,k in enumerate(baraja):
    tamaño = len(baraja)-i-1
    if k == "A" and tamaño>=1 and not (tiene_cartas_altas(baraja[i+1])):
        puntaje_actual = 1
    elif k == "J"and tamaño >= 2 and not (tiene_cartas_altas(baraja[i+1:i+3])):
        puntaje_actual = 2
    elif k == "Q" and tamaño >= 3 and not (tiene_cartas_altas(baraja[i+1:i+4])) :
        puntaje_actual = 3    
    elif k == "K" and tamaño>=4 and not (tiene_cartas_altas(baraja[i+1:i+5])):
        puntaje_actual = 4
    if puntaje_jugador == "jugador1":
        puntaje_jugador1 += puntaje_actual
        puntaje_jugador = "jugador2"
    else:
        puntaje_jugador2 += puntaje_actual
        puntaje_jugador = "jugador1"
    print(puntaje_jugador1,puntaje_jugador2)
    return puntaje_jugador1, puntaje_jugador2

juego(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'Q', 'K']*4)