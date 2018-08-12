from clases.Pantalla import *

class Colores(Pantalla):
	
	def __init__(self):
		
		self.config = 'windows'
		self.opciones = False 
		

	def lanzar(self , arg ):
		
		if arg[1] == 'fondo':

			color = ""

			if len(arg) < 3:
				color = 'azul'
			else:
				color = arg[2]

			self.fondo( self.getColor(color) )
		

	
