import os


class Pantalla():
	def __init__(self):
		pass 

	def fondo(self , color ):		
		os.system("color " + color )

	def cabezera(self , titulo ):		
		os.system("title  " + titulo )

	def titulo(self , titulo):

		print("\n\n\n " + titulo +  " \n\n")

	def comando(self):

		return input(" > ")





		