import random

def mezclar_baraja(baraja): 
    # Usar la función shuffle de random para mezclar la baraja en su lugar 
    random.shuffle(baraja) 
    return baraja

baraja_española = []  
#Definir los palos y los valores 
palos = ['oros', 'copas', 'espadas', 'bastos'] 
valores = [1, 2, 3, 4 , 5, 6, 7, 10 , 11, 12]  
#Crear las cartas 

# Variable para el ID 
id_carta = 1 

# Crear las cartas con ID 
for palo in palos: 
    for valor in valores: 
        carta = {'id': id_carta, 'palo': palo, 'valor': valor} 
        baraja_española.append(carta) 
        id_carta += 1
        

baraja_player1 = []
baraja_player2 = []

# print(baraja_española)

baraja_mezclada = mezclar_baraja(baraja_española)



for carta in baraja_mezclada:
    if len(baraja_player1) < 20:
        baraja_player1.append(carta)
    else:
        baraja_player2.append(carta)

print("jugador 1: ",baraja_player1)
print("jugador 2: ",baraja_player2)


duelo = 0
pozo_duelo = []

while len(baraja_player1) > 0 and len(baraja_player2) > 0:
    duelo += 1
    print('Batalla Nº:', duelo)
    if baraja_player1[0]['valor'] == 1 and baraja_player2[0]['valor'] == 12:
        print('Duelo ganado por player 1')
        baraja_player1.append(baraja_player1[0])
        baraja_player1.pop(0)
        baraja_player1.append(baraja_player2[0])
        baraja_player2.pop(0)
        baraja_player1.extend(pozo_duelo)
        pozo_duelo.clear()
        # print("jugador 1: ",baraja_player1)
        # print("jugador 2: ",baraja_player2)
        # print("pozo", pozo_duelo)
    elif baraja_player2[0]['valor'] == 1 and baraja_player1[0]['valor'] == 12:
        print('Duelo ganado por player 2')
        baraja_player2.append(baraja_player2[0])
        baraja_player2.pop(0)
        baraja_player2.append(baraja_player1[0])
        baraja_player1.pop(0)
        baraja_player2.extend(pozo_duelo)
        pozo_duelo.clear()
        # print("jugador 1: ",baraja_player1)
        # print("jugador 2: ",baraja_player2)
        # print("pozo", pozo_duelo)
    elif baraja_player1[0]['valor'] > baraja_player2[0]['valor']:
        print('Duelo ganado por player 1')
        baraja_player1.append(baraja_player1[0])
        baraja_player1.pop(0)
        baraja_player1.append(baraja_player2[0])
        baraja_player2.pop(0)
        baraja_player1.extend(pozo_duelo)
        pozo_duelo.clear()
        # print("jugador 1: ",baraja_player1)
        # print("jugador 2: ",baraja_player2)
        # print("pozo", pozo_duelo)
    elif baraja_player1[0]['valor'] < baraja_player2[0]['valor']:
        print('Duelo ganado por player 2')
        baraja_player2.append(baraja_player2[0])
        baraja_player2.pop(0)
        baraja_player2.append(baraja_player1[0])
        baraja_player1.pop(0)
        baraja_player2.extend(pozo_duelo)
        pozo_duelo.clear()
        # print("jugador 1: ",baraja_player1)
        # print("jugador 2: ",baraja_player2)
        # print("pozo", pozo_duelo)
    else:
        print('Duelo empatado')
        pozo_duelo.append(baraja_player1[0])
        baraja_player1.pop(0)
        pozo_duelo.append(baraja_player1[0])
        baraja_player1.pop(0)
        pozo_duelo.append(baraja_player2[0])
        baraja_player2.pop(0)
        pozo_duelo.append(baraja_player2[0])
        baraja_player2.pop(0)
        # print("jugador 1: ",baraja_player1)
        # print("jugador 2: ",baraja_player2)
        # print("pozo", pozo_duelo)

# print("jugador 1: ",baraja_player1)
# print("jugador 2: ",baraja_player2)
if len(baraja_player1) < 1:
    print('JUGADOR 2 HA GANADO LA GUERRA')
elif len(baraja_player2) < 1:
    print('JUGADOR 1 HA GANADO LA GUERRA')
