import os


class Pantalla():
	def __init__(self):
		pass

	def limpiar(self):
		os.system("cls")

	def pausa(self):
		os.system("pause > Kajataca 1.0")

	def ocultar(self):
		os.system("@echo off")

	def fondo(self , color ):		
		os.system("color " + color )

	def cabezera(self , titulo ):		
		os.system("title  " + titulo )

	def getColor(self , color):

		colores = {

			'rojo' : '4f' , 'azul' : '1f' , 
			'negro' : '0f' , 'cobalto' : '3f', 
			'morado' : '5f'

		}
		control = False

		for x in colores:
			
			if ( x == color):
				control = True

		if control == True: 
			return colores[color]
		else:
			return colores['negro']

		

	def titulo(self , titulo):

		print("\n\n\n " + titulo +  " \n\n")

	def comando(self):

		return input(" > ")


	def capturar_comandos(self , texto  ):
		
		captura = texto.split(" ")
		arg = {}
		arg[0] = 'kajataca'
		i = 1

		for x in captura:
			arg[i] = x
			i = i + 1

		return arg







		