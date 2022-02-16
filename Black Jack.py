import random
from termcolor import colored
import os

os.system('color')
cmd = 'cls'
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 
		  'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 
		  'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 0}
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Diamond', 'Hearts', 'Spades', 'Clubs')
is_game_on = True

class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank+' of '+self.suit
	
class Deck():
	def __init__(self):
		self.all_cards = []
		for suit in suits:
			for rank in ranks:
				created_card = Card(suit, rank)
				self.all_cards.append(created_card)

	def shuffle(self):
		random.shuffle(self.all_cards)

	def take_one(self):
		return self.all_cards.pop()

	def add_cards(self, new_cards):
		self.all_cards.append(new_cards)


class Player():
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
		self.all_cards = []

	def __str__(self):
		return f'Player {self.name} has a balance of: {self.balance}'

	def add_cards(self, new_cards):
		self.all_cards.append(new_cards)

	def remove_one(self):
		return self.all_cards.pop(0)

	def withdraw(self):
		if self.balance == 0:
			print('The amount you want to withdraw exceed the balance of this account.')
			is_game_on = False
		else:
			self.balance -= 10
			print('The amount of 10 has been withdraw from your account.')

	def deposit(self):
		self.balance += 20


class Dealer():
	def __init__(self, name):
		self.name = name
		self.all_cards = []

	def __str__(self):
		return f'Player {self.name} has {len(self.all_cards)} cards left.'

	def add_cards(self, new_cards):
		self.all_cards.append(new_cards)

	def remove_one(self):
		return self.all_cards.pop(0)

while(True):
	ace_value = int(input('Insert the value you want for the ace in this round. 1 or 14.\n'))
	if ace_value == 1:
		values['Ace'] = 1
		break
	elif ace_value == 14:
		values['Ace'] = 14
		break
	else:
		print('That is not a valid value for the ace. Try again')
deck = Deck()
player = Player('Abraham', 200)
dealer = Dealer('Dealer')
rounds_played = 0
while(is_game_on == True):
	while(True):
		if rounds_played == 0:
			break
		else:
			keep_playing = input('Enter S to stop playing or C to continue.\n')
			if keep_playing.upper() == 'S':
				is_game_on = False
				break
			elif keep_playing.upper() == 'C':
				break
			else:
				print('That is not a valid option. Try again.')
	if is_game_on == False:
		break
	deck.shuffle()
	summatory_player = 0
	summatory_dealer = 0
	player.withdraw()
	print(player)
	for i in range(2):
		player.add_cards(deck.take_one())
		dealer.add_cards(deck.take_one())
	print(f'Initial cards for {player.name}: {player.all_cards[0]} and {player.all_cards[1]}')
	print(f'{dealer} One card is: {dealer.all_cards[0]}')
	for item in player.all_cards:
		summatory_player += item.value
	for item in dealer.all_cards:
		summatory_dealer += item.value
	input('Enter any key to continue.')
	os.system(cmd)

	while(True):
		if summatory_player <= 21 and summatory_dealer <= 21:
			print(f'{player.name} summatory: {summatory_player}')
			print(f'{dealer.name} known summatory: {dealer.all_cards[0].value}')
			choice = input('Enter H to receive another card or S to stop receiving cards.\n')
			os.system(cmd)
			
			if choice.upper() == 'H':
				player.add_cards(deck.take_one())
				dealer.add_cards(deck.take_one())
				print(f"New card added to {player.name}'s deck: {player.all_cards[-1]}")
				summatory_player += player.all_cards[-1].value
				summatory_dealer += dealer.all_cards[-1].value
			
			elif choice.upper() == 'S':
				if summatory_player > summatory_dealer:
					print(colored(f'Cards of {player.name}', 'green'))
					for item in player.all_cards:
						print(item)
					print(colored(f'Cards of {dealer.name}', 'green'))
					for item in dealer.all_cards:
						print(item)
					print(f'{player.name} summatory: {summatory_player}')
					print(f'{dealer.name} summatory: {summatory_dealer}')
					print(colored(f'{player.name} won this round.', 'red'))
					player.deposit()
					while(len(player.all_cards) > 0 and len(dealer.all_cards) > 0):
						deck.add_cards(player.remove_one())
						deck.add_cards(dealer.remove_one())
					rounds_played += 1
					break

				elif summatory_player < summatory_dealer:
					print(colored(f'Cards of {player.name}', 'green'))
					for item in player.all_cards:
						print(item)
					print(colored(f'Cards of {dealer.name}', 'green'))
					for item in dealer.all_cards:
						print(item)
					print(f'{player.name} summatory: {summatory_player}')
					print(f'{dealer.name} summatory: {summatory_dealer}')
					print(colored(f'{dealer.name} won this round.', 'red'))
					while(len(player.all_cards) > 0 and len(dealer.all_cards) > 0):
						deck.add_cards(player.remove_one())
						deck.add_cards(dealer.remove_one())
					rounds_played += 1
					break

				else:
					print(colored(f'Cards of {player.name}', 'green'))
					for item in player.all_cards:
						print(item)
					print(colored(f'Cards of {dealer.name}', 'green'))
					for item in dealer.all_cards:
						print(item)
					print(f'{player.name} summatory: {summatory_player}')
					print(f'{dealer.name} summatory: {summatory_dealer}')
					print(colored('No one won this round', 'red'))
					while(len(player.all_cards) > 0 and len(dealer.all_cards) > 0):
						deck.add_cards(player.remove_one())
						deck.add_cards(dealer.remove_one())
					rounds_played += 1
					break
			else:
				print('That is not a valid option. Try again.')

		elif summatory_player > 21:
			print(colored(f'Cards of {player.name}', 'green'))
			for item in player.all_cards:
				print(item)
			print(colored(f'Cards of {dealer.name}', 'green'))
			for item in dealer.all_cards:
				print(item)
			print(f'{player.name} summatory: {summatory_player}')
			print(f'{dealer.name} summatory: {summatory_dealer}')
			print(colored(f'It seems like {player.name} has lost.', 'red'))
			while(len(player.all_cards) > 0 and len(dealer.all_cards) > 0):
				deck.add_cards(player.remove_one())
				deck.add_cards(dealer.remove_one())
			rounds_played += 1
			break

		else:
			print(colored(f'Cards of {player.name}', 'green'))
			for item in player.all_cards:
				print(item)
			print(colored(f'Cards of {dealer.name}', 'green'))
			for item in dealer.all_cards:
				print(item)
			print(f'{player.name} summatory: {summatory_player}')
			print(f'{dealer.name} summatory: {summatory_dealer}')
			print(colored(f'It seems like {dealer.name} has lost.', 'red'))
			player.deposit()
			while(len(player.all_cards) > 0 and len(dealer.all_cards) > 0):
				deck.add_cards(player.remove_one())
				deck.add_cards(dealer.remove_one())
			rounds_played += 1
			break