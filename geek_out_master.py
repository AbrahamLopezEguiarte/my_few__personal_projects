import random

valor_cara = {1:'heroe', 2:'meeple', 3:'dragon', 4:'nave', 5:'corazon', 6:'42'}
caras = [1, 2, 3, 4, 5, 6]

class Caras_de_dados():
	def __init__(self):
		self.valor = caras[0::]

	def __str__(self):
		for obj in self.valor:
			return f'obj{self.valor}'

class Dados_activos():
	def __init__(self):
		self.dados_activos = []
		for dado in range(10):
			for i in range(1, 7):
				created_dice = Caras_de_dados()
			self.dados_activos.append(created_dice)

	def __len__(self):
		return len(self.dados_activos)

	def remover_uno(self):
		return self.dados_activos.pop(0)

	def shuffle_dados(self):
		index = 0
		for obj in range(10):
			random.shuffle(dados.dados_activos[index].valor)
			index+=1

	def mostrar_caras(self):
		index = 0
		while(True):
			if index > len(self.dados_activos)-1:
				break
			else:
				aux = random.randint(0, 5)
				if index != len(self.dados_activos)-1:
					print(valor_cara[dados.dados_activos[index].valor[aux]], end=" , ")
				else:
					print(valor_cara[dados.dados_activos[index].valor[aux]], end="\n")
				index+=1


class Dados_inactivos():
	def __init__(self):
		self.dados_inactivos = []
	
	def introducir_dados(self, dados):
		self.dados_inactivos.append(dados)
	
	def __len__(self):
		return len(self.dados_inactivos)

#class Dados_utilizados():
#	def __init__(self):
#		self.dados_utilizados = []
	
#	def introducir_dados(self, dados):
#		self.dados_utilizados.extend(dados)
	
#	def __len__(self):
#		return len(self.dados_utilizados)

dados = Dados_activos()
contenedor_dados_inactivos = Dados_inactivos()
dados.shuffle_dados()
while(True):
	if len(contenedor_dados_inactivos) != 3:
		contenedor_dados_inactivos.introducir_dados(dados.remover_uno())
	else:
		break
print("Dados inactivos: "+str(len(contenedor_dados_inactivos)))
print("Dados activos: "+str(len(dados.dados_activos)))
print("Caras de los dados activos: ")
dados.mostrar_caras()