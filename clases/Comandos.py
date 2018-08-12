# Clase para comandos MS-DOS & Linux (No orientado a presentacion)
import os

class Comandos():
	"""docstring for Comandos"""
	def __init__(self):
		pass

	def lanzar(self , arg):

		texto = ""
		arg[0] = ""
		
		for t in arg:
			texto = texto + " " + t	
		
		os.system(texto)
		