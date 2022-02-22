import random

# Diccionario que se utiliza para tener acceso a las correspondientes caras de los dados
valor_cara = {1:'heroe', 2:'meeple', 3:'dragon', 4:'nave', 5:'corazon', 6:'42'}
# Valor numérico para cada una de las caras de los dados
caras = [1, 2, 3, 4, 5, 6]

class CarasDeDados():
	# Método utilizado para asignar las caras a un nuevo dado
	def __init__(self):
		self.valor = caras[0::]

	def __str__(self):
		for obj in self.valor:
			return f'obj{self.valor}'

class DadosActivos():
	# método utilizado para asignar las caras a los 10 dados que se utilizan en el juego por medio de objetos de tipo Caras_de_dados
	def __init__(self):
		self.dados_activos = []
		for dado in range(10):
			for i in range(1, 7):
				created_dice = CarasDeDados()
			self.dados_activos.append(created_dice)

	def __len__(self):
		return len(self.dados_activos)
	
	# Método para remover un dado del estado activo
	def remover_uno(self, dado_activado):
		return self.dados_activos.pop(dado_activado)
	
	# Método para acomodar las caras de los dados al azar. Será actualizada para que sea utilizada para hacer una tirada
	def shuffle_dados(self):
		index = 0
		for obj in range(10):
			random.shuffle(self.dados_activos[index].valor)
			index+=1
	
	# Método para mostrar una de las caras de los dados activos. Será actualizada para mostrar la cara resultante al hacer una tirada
	def mostrar_caras(self):
		index = 0
		while(True):
			if index <= len(self.dados_activos)-1:
				aux = 0
				if index != len(self.dados_activos)-1:
					print(valor_cara[self.dados_activos[index].valor[aux]]+f' ({index})', end=" , ")
				else:
					print(valor_cara[self.dados_activos[index].valor[aux]]+f' ({index})', end="\n")
				index+=1
			else:
				break

class DadosInactivos():
	# Método para crear un "contenedor" para los dados inactivos
	def __init__(self):
		self.dados_inactivos = []
	
	# Método utilizado para añadir tres dados activos al inicio del juego
	def introducir_dados(self, dados):
		self.dados_inactivos.append(dados)
	
	def __len__(self):
		return len(self.dados_inactivos)

class DadosUtilizados():
	def __init__(self):
		self.dados_utilizados = []

	def introducir_dados(self, dados):
		self.dados_utilizados.append(dados)
	
	def __len__(self):
		return len(self.dados_utilizados)

	def activar_dado(self, dado_a_activar):
		if valor_cara[dados.dados_activos[dado_a_activar].valor[0]] == valor_cara[1]:
			self.introducir_dados(dados.remover_uno(dado_a_activar))
			dados.mostrar_caras()
			dado_a_girar = int(input('Seleccione el dado que desea girar: '))
			if dados.dados_activos[dado_a_girar].valor[0] == 1:
				dados.dados_activos[dado_a_girar].valor[0] = 3
			elif dados.dados_activos[dado_a_girar].valor[0] == 2:
				dados.dados_activos[dado_a_girar].valor[0] = 4
			elif dados.dados_activos[dado_a_girar].valor[0] == 3:
				dados.dados_activos[dado_a_girar].valor[0] = 1
			elif dados.dados_activos[dado_a_girar].valor[0] == 4:
				dados.dados_activos[dado_a_girar].valor[0] = 2
			elif dados.dados_activos[dado_a_girar].valor[0] == 5:
				dados.dados_activos[dado_a_girar].valor[0] = 6
			elif dados.dados_activos[dado_a_girar].valor[0] == 6:
				dados.dados_activos[dado_a_girar].valor[0] = 5
				
		elif valor_cara[dados.dados_activos[dado_a_activar].valor[0]] == valor_cara[2]:
			self.introducir_dados(dados.remover_uno(dado_a_activar))
			dados.mostrar_caras()
			dado_a_tirar = int(input('Seleccione el dado que desea volver a tirar: '))
			random.shuffle(dados.dados_activos[dado_a_tirar].valor)
		
		#elif valor_cara[dados.dados_activos[dado_a_activar].valor[0]] == valor_cara[3]:
		elif valor_cara[dados.dados_activos[dado_a_activar].valor[0]] == valor_cara[4]:
			self.introducir_dados(dados.remover_uno(dado_a_activar))
			dados.mostrar_caras()
			dado_a_destruir = int(input('Seleccione el dado que desea destruir: '))
			self.introducir_dados(dados.remover_uno(dado_a_destruir))

dados = DadosActivos()
contenedor_dados_inactivos = DadosInactivos()
contenedor_dados_utilizados = DadosUtilizados()
dados.shuffle_dados()
while(True):
	if len(contenedor_dados_inactivos) != 3:
		contenedor_dados_inactivos.introducir_dados(dados.remover_uno(0))
	else:
		break
print("Dados inactivos: "+str(len(contenedor_dados_inactivos)))
print("Dados activos: "+str(len(dados.dados_activos)))
print("Caras de los dados activos: ")
dados.mostrar_caras()
dado_seleccionado = int(input('Ingrese el dado que desea activar: '))
contenedor_dados_utilizados.activar_dado(dado_seleccionado)
dados.mostrar_caras()
print("Dados inactivos: "+str(len(contenedor_dados_inactivos)))
print("Dados activos: "+str(len(dados)))
print("Dados utilizados: "+str(len(contenedor_dados_utilizados)))