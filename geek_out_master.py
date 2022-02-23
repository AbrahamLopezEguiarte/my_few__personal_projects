import random
import os

clear = lambda: os.system('cls')

# Diccionario que se utiliza para tener acceso a las correspondientes caras de los dados
valor_cara = {1:'heroe', 2:'meeple', 3:'dragon', 4:'nave', 5:'corazon', 6:'42'}
# Valor numérico para cada una de las caras de los dados
caras = [1, 2, 3, 4, 5, 6]

class Puntaje():
	def __init__(self):
		self.casillas_ocupadas = []
		self.puntaje = 0

	def __len__(self):
		return len(self.casillas_ocupadas)
	
	def agregar_casilla_ocupada(self, cantidad_casillas):
		self.casillas_ocupadas.extend(cantidad_casillas)
	
	def calcular_puntaje(self):
		if len(self.casillas_ocupadas) == 0:
			pass
		else:
			self.puntaje = self.casillas_ocupadas[len(self.casillas_ocupadas)-1] + self.puntaje
	
	def __str__(self):
		return f'El puntaje es: {self.puntaje}'

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

	def introducir_dados(self, dados):
		self.dados_activos.append(dados)
	
	# Método para acomodar las caras de los dados de forma aleatoria, simulando una tirada
	def shuffle_dados(self):
		index = 0
		for obj in range(10):
			random.shuffle(self.dados_activos[index].valor)
			index+=1
	
	# Método para mostrar la cara inicial de cada dado después de simular una tirada con shuffle_dados
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
	
	def remover_uno(self):
		return self.dados_inactivos.pop(0)
	
	def __len__(self):
		return len(self.dados_inactivos)

class DadosUtilizados():
	# Método para crear un "contenedor" para los dados utilizados
	def __init__(self):
		self.dados_utilizados = []

	# Método utilizado para añadir los dados que han sido utilizados
	def introducir_dados(self, dados):
		self.dados_utilizados.append(dados)
	
	def __len__(self):
		return len(self.dados_utilizados)

	# Método utilizado para hacer uso de la función especial de cada dado al utilizarlo
	def activar_dado(self, dado_a_activar):
		clear()
		
		if dado_a_activar < 0 or dado_a_activar > 6:
			print('Ese no es un valor adecuado, ingrese otro')

		elif valor_cara[dados.dados_activos[dado_a_activar].valor[0]] == valor_cara[1]:
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
		
		elif valor_cara[dados.dados_activos[dado_a_activar].valor[0]] == valor_cara[3]:
			dados.mostrar_caras()
			dado_a_utilizar = int(input('Este dado no puede utilizarse a menos que sea el último dado activo. Ingrese otro dado para utilizar: '))
			contenedor_dados_utilizados.activar_dado(dado_a_utilizar)

		elif valor_cara[dados.dados_activos[dado_a_activar].valor[0]] == valor_cara[4]:
			self.introducir_dados(dados.remover_uno(dado_a_activar))
			dados.mostrar_caras()
			dado_a_destruir = int(input('Seleccione el dado que desea destruir: '))
			self.introducir_dados(dados.remover_uno(dado_a_destruir))
		
		elif valor_cara[dados.dados_activos[dado_a_activar].valor[0]] == valor_cara[5]:
			self.introducir_dados(dados.remover_uno(dado_a_activar))
			if len(contenedor_dados_inactivos) > 0:
				dados.introducir_dados(contenedor_dados_inactivos.remover_uno())
				print('Un dado inactivo ha sido activado')
				random.shuffle(dados.dados_activos[-1].valor)
			else:
				print('No hay más dados inactivos. No se agregaron dados')
		
		else:
			dados.mostrar_caras()
			dado_a_utilizar = int(input('Este dado no puede utilizarse a menos que sea el último dado activo. Ingrese otro dado para utilizar: '))
			contenedor_dados_utilizados.activar_dado(dado_a_utilizar)


dados = DadosActivos()
contenedor_dados_inactivos = DadosInactivos()
contenedor_dados_utilizados = DadosUtilizados()
puntaje = Puntaje()
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
while(True):
	if len(dados.dados_activos) == 0:
		clear()
		print('Te quedaste sin dados activos. La partida finalizó')
		break

	elif len(dados.dados_activos) == 1:
		if valor_cara[dados.dados_activos[0].valor[0]] == valor_cara[1]:
			print('Te quedaste sin dados activos. La partida finalizó')
			break

		elif valor_cara[dados.dados_activos[0].valor[0]] == valor_cara[2]:
			print('Te quedaste sin dados activos. La partida finalizó')
			break

		elif valor_cara[dados.dados_activos[0].valor[0]] == valor_cara[3]:
			print('Te quedaste sin dados activos. La partida finalizó')
			break

		elif valor_cara[dados.dados_activos[0].valor[0]] == valor_cara[4]:
			print('Te quedaste sin dados activos. La partida finalizó')
			break
		elif valor_cara[dados.dados_activos[0].valor[0]] == valor_cara[5]:
			print('Te quedaste sin dados activos. La partida finalizó')
			break
		elif valor_cara[dados.dados_activos[0].valor[0]] == valor_cara[6]:
			print('Te quedaste sin dados activos. La partida finalizó')
			break
	
	else:
		dado_seleccionado = int(input('Ingrese el dado que desea activar: '))
		contenedor_dados_utilizados.activar_dado(dado_seleccionado)
		dados.mostrar_caras()
		print("Dados inactivos: "+str(len(contenedor_dados_inactivos)))
		print("Dados activos: "+str(len(dados)))
		print("Dados utilizados: "+str(len(contenedor_dados_utilizados)))