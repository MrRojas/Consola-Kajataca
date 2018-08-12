from clases.Conexion import *
from clases.Pantalla import *

class Mensajes(Conexion):
	
	def __init__(self, arg):

		self.nombre_db = 'C:/AppServ/www/consola/storage/armando.db'
		
		# Nuevo mensaje 
		if(arg[2] == '-n'):
			self.nuevoMensaje(arg)

		if(arg[2] == '-v'):
			self.verMensajes(arg)

	def capturarTexto (self , arg):
		
		i = 0
		texto = ""

		for x in arg:
			
			i = i + 1 

			if(i > 3):
				texto = texto + ' ' + x  

		return texto 

	def nuevoMensaje(self , arg ):

		texto = self.capturarTexto(arg)
		
		clave = self.ejecutar("SELECT count(ID) FROM  mensajes ")

		for x in clave:
			clave = x[0]

	

		sql = "INSERT INTO mensajes VALUES ( " + str (clave + 1) + " , '" + texto + "' )" 

		self.ejecutar( sql )


	def verMensajes(self , arg):

		pantalla = Pantalla()

		sql = "SELECT * FROM mensajes"; 

		datos = self.ejecutar(sql)

		print("## Mensajes... \n\n ")

		for x in datos:
			
			print("\n Mensaje = ", x[1])

		pantalla.fondo('4f')
		pantalla.pausa()



		







