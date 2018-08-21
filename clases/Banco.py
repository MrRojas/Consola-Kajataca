from clases.Conexion import *

class Banco(Conexion):
	"""docstring for Banco"""
	def __init__(self, arg):
		super(Banco, self).__init__()
		pass


	def registrar(self , arreglo ):
		
		sql = "INSERT INTO bancos (descripcion, cabezera, numero_row )" 
		sql = sql + " VALUES ( '{0}' , '{1}' , '{2}' )  ".format( arreglo['descripcion'] , arreglo['cabezera'] , arreglo['numero_row']  )

		self.ejecutar(sql)



		