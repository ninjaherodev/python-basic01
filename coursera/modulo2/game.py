'''
🤖 Juego de Piedra, Papel y Tijera

'''
import random

opciones = ('piedra', 'papel', 'tijera')
opciones_text = ', '.join(opciones).title()
COLOR_ROJO = "\033[91m"
RESET_COLOR = "\033[0m"

def turnUser():
    eleccion = input(f'Elige [{opciones_text}]:').lower()
    while eleccion not in opciones:
         print(f"{COLOR_ROJO}\n❌ Entrada no válida. Inténtalo de nuevo. \n{RESET_COLOR}")
         eleccion = input(f'Elige [{opciones_text}]:').lower()
    return eleccion

def turnCpu():
    return random.choice(opciones)

def winner(opcUser, opcCpu):
    if(opcUser == opcCpu):
        return '¡Empate!'
    victorias = {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel"
    }
    return "¡Ganaste!" if victorias[opcUser] == opcCpu else '¡Perdiste!'

def game():
    roundsPlayed  = 0
    while roundsPlayed < 3:
        usuario = turnUser()
        cpu = turnCpu()
        print(f'{usuario} V.S {cpu}')
        mensaje = winner(usuario, cpu)
        print(mensaje)
        roundsPlayed +=1
   
   

if __name__ == '__main__':
   game()