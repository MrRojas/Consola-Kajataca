from clases.Pantalla import *
from clases.Colores import *
from clases.Comandos import *
from clases.Mensajes import *

class Menu(Pantalla):
	
	def __init__(self):
		
		self.cabezera('Kajataca')
		
		pass 

	def add_argumentos(self , arg ):
		self.arg = arg

	def principal(self):

		self.ocultar()
		self.limpiar()
		self.fondo('4f')
		self.titulo(" CLI Kajataca 1.0...")
		return self.comando()

	def lanzar_evento(self):
		
		if self.arg[1] == 'fondo':
			colores = Colores()
			colores.lanzar(self.arg)
		elif self.arg[1] == 'pausa':
			self.pausa()
		elif self.arg[1] == 'limpiar':
			self.limpiar()
		elif self.arg[1] == 'msg':
			msg = Mensajes(self.arg)
		else:
			comandos = Comandos()
			comandos.lanzar(self.arg)

	


		