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

	def remover_uno(self):
		return self.all_dice.pop(0)

class Dados_inactivos():
	def __init__(self):
		self.dados_inactivos = []
	
	def introducir_dados(self, dados):
		self.dados_inactivos.append(dados)
	
	def __len__(self):
		return len(self.dados_inactivos)

#class Dados_activos():
#	def __init__(self):
#		self.dados_activos = []
	
#	def introducir_dados(self, dados):
#		self.dados_activos.extend(dados)
	
#	def __len__(self):
#		return len(self.dados_activos)

dados = Dados()
contenedor_dados_inactivos = Dados_inactivos()
index = 0
for obj in range(10):
	random.shuffle(dados.all_dice[index].valor)
	index+=1
print(len(contenedor_dados_inactivos))
print(len(dados.all_dice))
aux = 0
print("Dados antes de enviar tres a inactivos")
while(True):
	if aux <= 9:
		print(dados.all_dice[aux].valor[0::])
		aux+=1
	else:
		aux = 0
		break
while(True):
	if len(contenedor_dados_inactivos) != 3:
		contenedor_dados_inactivos.introducir_dados(dados.remover_uno())
	else:
		break
print(len(contenedor_dados_inactivos))
print(len(dados.all_dice))
print("Dados después de enviar tres a inactivos")
while(True):
	if aux < len(dados.all_dice):
		print(dados.all_dice[aux].valor[0::])
		aux+=1
	else:
		aux = 0
		break
print("Dados inactivos")
while(True):
	if aux < len(contenedor_dados_inactivos):
		print(contenedor_dados_inactivos.dados_inactivos[aux].valor[0::])
		aux+=1
	else:
		break

#print(dados.all_dice[0].valor[0::])
#print(dados.all_dice[1].valor[0::])
#print(dados.all_dice[2].valor[0::])
#print(dados.all_dice[3].valor[0::])
#print(dados.all_dice[4].valor[0::])
#print(dados.all_dice[5].valor[0::])
#print(dados.all_dice[6].valor[0::])
#print(dados.all_dice[7].valor[0::])
#print(dados.all_dice[8].valor[0::])
#print(dados.all_dice[9].valor[0::])

#cara = random.randint(0, 5)
#print(cara)
#print(valor_cara[dados.all_dice[0].valor[cara]])