"""
	Conexion A Base de Datos SQLite3 !! Armando Rojas !! 12-08-2018
"""
import sqlite3

class Conexion():
	
	def __init__(self, nombre_db = 'storage/armando.db' ):
		
		self.nombre_db = nombre_db 
		pass 

	def ejecutar(self , sql ):

		con = sqlite3.connect(self.nombre_db)
		cursor = con.cursor()
		data = {}
		
		cursor.execute(sql)

		if sql[0] == "S":
			
			return cursor
				
		else:
			con.commit()
			data = con.total_changes
			con.close()
	

		return data

	def cerrar(self):
		
		self.con.close()
		

	