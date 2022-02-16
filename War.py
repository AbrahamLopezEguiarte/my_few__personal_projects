# Importamos el módulo random, el cual utilizaremos después para mezclar nuestro mazo.
import random
from termcolor import colored
import os
os.system('color')

# Inicializa un diccionario que utilizaremos para poder comparar los valores de las cartas durante el juego, siendo capaces
# de mandar una cadena a la clase y con ello poder acceder a un valor numérico que podamos comparar.
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 
		  'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 
		  'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
# Inicializa una tupla que contenga los nombres en forma de cadena de cada una de las cartas que utilizaremos en el juego
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# Inicializa una tupla que contenga los cuatro tipos de cartas que utilizaremos en el juego.
suits = ('Diamond', 'Hearts', 'Spades', 'Clubs')
# Inicializa una variable booleana que nos ayudará a detectar cuando el juego siga corriendo, es decir, que ningún jugador se
# haya quedado sin cartas en su mazo.
is_game_on = True

# Define una clase llamada Card con la cual seremos capaces de asignar un tipo de carta y un valor en forma de string.
# Con esto podremos asignar un valor numérico al objeto en cuestión.
class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank+' of '+self.suit

# Define una clase llamada Deck que nos servirá para generar un nuevo mazo en cada partida.
class Deck():
	# Define un método en el cual se crea una lista vacía. Dicha lista será llenada con objetos de la clase Card.
	# Dichos objetos obtendrán un valor y un tipo de carta, generando así un mazo de 52 cartas.
	# Cada uno de estos objetos serán un objeto llamado "created_card", el cual se agrega uno por uno a la lista anteriormente
	# creada.
	def __init__(self):
		self.all_cards = []
		for suit in suits:
			for rank in ranks:
				created_card = Card(suit, rank)
				self.all_cards.append(created_card)

	# Define un método llamado shuffle que nos servirá para mezclar el mazo de manera aleatoria en cada nuevo juego utilizando
	# la función "shuffle" del módulo "random"
	def shuffle(self):
		random.shuffle(self.all_cards)

	# Define un método llamado take_one con el cual retornaremos uno de los objetos de nuestra lista, es decir, una carta.
	# Para esto utilizamos el método "pop".
	def take_one(self):
		return self.all_cards.pop()

# Define una clase llamada Player con la cual podremos controlar las acciones del jugador tales como asignarle un nombre,
# remover una carta del mazo o agregar cartas nuevas a este.
class Player():
	def __init__(self, name):
		self.name = name
		self.all_cards = []

	# Define un método llamado remove_one con el cual utilizamos la función "pop" para eliminar la carta de la cima del mazo.
	def remove_one(self):
		return self.all_cards.pop(0)

	# Define un método llamado add_cards con la cual podremos agregar una o varias cartas al mazo del jugador.
	def add_cards(self, new_cards):
		if type(new_cards) == type([]):
			self.all_cards.extend(new_cards)
		else:
			self.all_cards.append(new_cards)

	def __str__(self):
		return f'Player {self.name} has {len(self.all_cards)} cards left'

# Creamos un objeto de la clase Deck.
deck = Deck()

# Llamamos al método shuffle_deck.
deck.shuffle()

# Creamos los objetos player_1 y player_2 de la clase Player.
player_1 = Player('Abraham')
player_2 = Player('Cory')

# Repartimos las cartas entre los jugadores.
for item in range(26):
	player_1.add_cards(deck.take_one())
	player_2.add_cards(deck.take_one())

# Imprimimos ambos objetos Player para asegurarnos que se hayan divido correctamente las cartas
print(colored(player_1, 'white'))
print(colored(player_2, 'white'))

# Contador con la cantidad de rondas
round_game = 0

# Ciclo para mantener el juego corriendo
while is_game_on:

	round_game += 1
	print(colored(f'Round number: {round_game}', 'cyan'))
	
	# Si el jugador se queda sin cartas marcará que ha perdido y terminará el juego
	if len(player_1.all_cards) == 0:
		print(f'{player_1.name} has run out of cards. {player_2.name} wins')
		is_game_on = False

	elif len(player_2.all_cards) == 0:
		print(f'{player_1.name} has run out of cards. {player_2.name} wins')
		is_game_on = False
	
	# Si ambos jugadores tienen cartas entonces el juego comienza, creando dos listas, una para cada jugador.
	# En ellas se agrega la carta que se saca
	else:
		player_1_cards = []
		player_1_cards.append(player_1.remove_one())
		player_2_cards = []
		player_2_cards.append(player_2.remove_one())

		# Se inicializa una variable booleana para entrar en "guerra" y así verificar los valores de las cartas
		at_war = True

		while(at_war == True):

			# Si la carta del mazo creado anteriormente del jugador 1 es mayor entonces se añade su carta y
			# la del jugador 2 a su mazo original y se cambia "at_war" a falso para seguir sacando cartas
			if player_1_cards[-1].value > player_2_cards[-1].value:
				print(colored(f"{player_1.name}'s card is: {player_1_cards[-1]}", 'green'))
				print(colored(f"{player_2.name}'s card is: {player_2_cards[-1]}", 'green'))
				print(colored(f'{player_1.name} wins this round', 'yellow'))
				player_1.add_cards(player_1_cards)
				player_1.add_cards(player_2_cards)
				at_war = False

			# Si la carta del mazo creado anteriormente del jugador 2 es mayor entonces se añade su carta y
			# la del jugador 1 a su mazo original y se cambia "at_war" a falso para seguir sacando cartas
			elif player_1_cards[-1].value < player_2_cards[-1].value:
				print(colored(f"{player_1.name}'s card is: {player_1_cards[-1]}", 'green'))
				print(colored(f"{player_2.name}'s card is: {player_2_cards[-1]}", 'green'))
				print(colored(f'{player_2.name} wins this round', 'magenta'))
				player_2.add_cards(player_2_cards)
				player_2.add_cards(player_1_cards)
				at_war = False

			# En caso de ambas cartas ser del mismo valor se entra en guerra y ambos jugadores extraerán
			# un total de 5 cartas de su mazo original que se añadirán a su mazo anteriormente creado,
			# siempre y cuando tengan cartas suficientes (de lo contrario perderán) y entonces el ciclo se repite
			# con la última carta añadida
			else:
				print(colored('At war!', 'red'))
				if len(player_1.all_cards) < 5:
					print(f'{player_1.name} has run out of cards. {player_2.name} wins')
					is_game_on = False
					break

				elif len(player_2.all_cards) < 5:
					print(f'{player_2.name} has run out of cards. {player_1.name} wins')
					is_game_on = False
					break

				else:
					for num in range(5):
						player_1_cards.append(player_1.remove_one())
						player_2_cards.append(player_2.remove_one())