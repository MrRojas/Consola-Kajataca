from clases.Pantalla import *
from clases.Colores import *
from clases.Comandos import *
from clases.Mensajes import *
from clases.Banco import *
 
class Menu(Pantalla):
	
	def __init__(self):
		
		self.cabezera('Kajataca')

		self.control = 0
		
		pass 

	def add_argumentos(self , arg ):
		self.arg = arg

	def principal(self):

		if self.control == 0:

			self.ocultar()
			self.limpiar()
			self.fondo('4f')
			self.titulo(" CLI Kajataca 1.0...")

			self.control = 1
		
		comando = self.comando()

		self.add_argumentos( self.capturar_comandos(comando) )
		self.lanzar_evento()

		return comando

	def lanzar_evento(self):

		if self.arg[1] == 'fondo':
			colores = Colores()
			colores.lanzar(self.arg)
		elif self.arg[1] == 'pausa':
			self.pausa()
		elif self.arg[1] == 'limpiar':
			self.limpiar()
		elif (self.arg[1] == 'msg') or (self.arg[1] == '-m'):
			msg = Mensajes(self.arg)
		elif( self.arg[1] == 'ms-dos' ):
			comandos = Comandos()
			comandos.lanzar(self.arg)
		elif( self.arg[1] == 'exit' )  or ( self.arg[1] == 'salir' ):
			print ("Adios...")
		elif( self.arg[1] == 'banco' ):
			arreglo = { 'descripcion' : 'Ok' , 'cabezera' : 'Ok2..' , 'numero_row' : 'Ok3'   }
			banco = Banco(self.arg)
			banco.registrar(arreglo)

		else:
			print("Comando no encontrado")
			


	


		