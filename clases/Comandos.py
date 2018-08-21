# Clase para comandos MS-DOS & Linux (No orientado a presentacion)
import os

class Comandos():
	"""docstring for Comandos"""
	def __init__(self):
		pass

	def lanzar(self , arg):

		texto = ""
		arg[0] = ""
		arg[1] = ""
		i = 0
		
		for t in arg:
			texto = texto + " " + arg[i]
			i = 1 + i 	
		
		os.system(texto)


	def buscar(self):
		pass


	def nuevo(self):
		pass
		