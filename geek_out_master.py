import random

valor_cara = {1:'heroe', 2:'meeple', 3:'dragon', 4:'nave', 5:'corazon', 6:'42'}
#figura_cara = ('heroe', 'meeple', 'dragon', 'nave', 'corazon', '42')
caras = [1, 2, 3, 4, 5, 6]

class Caras_de_dados():
	def __init__(self):
		self.valor = caras[0::]

	def __str__(self):
		for obj in self.valor:
			return f'obj{self.valor}'

class Dados():
	def __init__(self):
		self.all_dice = []
		for dado in range(10):
			for i in range(1, 7):
				created_dice = Caras_de_dados()
			self.all_dice.append(created_dice)

	def __len__(self):
		return len(self.all_dice)

dados = Dados()
index = 0
for obj in range(10):
	random.shuffle(dados.all_dice[index].valor)
	index+=1
print(dados.all_dice[0].valor[0::])
print(dados.all_dice[1].valor[0::])
print(dados.all_dice[2].valor[0::])
print(dados.all_dice[3].valor[0::])
print(dados.all_dice[4].valor[0::])
print(dados.all_dice[5].valor[0::])
print(dados.all_dice[6].valor[0::])
print(dados.all_dice[7].valor[0::])
print(dados.all_dice[8].valor[0::])
print(dados.all_dice[9].valor[0::])

cara = random.randint(0, 5)
print(cara)
print(valor_cara[dados.all_dice[0].valor[cara]])