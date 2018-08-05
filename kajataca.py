###################################################
# CLI Kajataca para Gestionar Actividades en PC   #
###################################################
import sys 
from clases.Menu import *



if( len(sys.argv) < 2 ):
	menu = Menu()
	menu.principal()
else:

	opciones = sys.argv
	
	print(opciones[1])

