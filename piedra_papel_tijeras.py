import random


def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"



def jugar_torneo():
    print("-"*30, "Bienvenido al juego de Piedra, Papel o Tijeras", "-"*30)
    print("*"*80)
    print("                     Ganará el primero en llegar a 3 puntos")
    print("*"*80)
    puntos_usuario = 0
    puntos_ordenador = 0
    
    while puntos_usuario < 3 and puntos_ordenador < 3:
        print(f"Puntuación: Usuario {puntos_usuario} - Ordenador {puntos_ordenador}")
        
        eleccion_ordenador = ordenador_decide_jugada()
        eleccion_usuario = usuario_decide_jugada()
        
        print(f"El ordenador eligió: {eleccion_ordenador}")
        print("*"*80)
        resultado = determina_ganador(eleccion_usuario, eleccion_ordenador)
        print(f"Resultado de la ronda: {resultado}")
        print("*"*80)
        if resultado == "Ganaste":
            puntos_usuario += 1
        elif resultado == "Perdiste":
            puntos_ordenador += 1
    
    if puntos_usuario == 3:
        print("ganaste la partida!")
    else:
        print("El ordenador ganó la partida...")

if __name__ == "__main__":
    jugar_torneo()